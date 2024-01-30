using UnityEngine;

public class BrickParenting : MonoBehaviour
{
    public GameObject parentCube;
    public ID idObj;

    public bool scriptEnabled = false;

    private void OnTriggerEnter(Collider other)
    {
        var tempID = other.GetComponent<IDContainerBehavior>();
        if (tempID == null)
            return;

        var otherID = tempID.idObj;
        if (otherID == idObj && scriptEnabled)
        {
            Transform currentParent = other.transform.parent;

            // Traverse the parent hierarchy until reaching the topmost parent with the proper idObj
            while (currentParent != null)
            {
                var parentID = currentParent.GetComponent<IDContainerBehavior>();
                if (parentID != null && parentID.idObj == idObj)
                    break;

                currentParent = currentParent.parent;
            }

            // Set the entering object as a child of the topmost parent with the proper idObj
            if (currentParent != null)
            {
                parentCube.transform.parent = currentParent;

                Rigidbody parentRigidbody = parentCube.GetComponent<Rigidbody>();
                parentRigidbody.isKinematic = true;
            }
        }
    }

    public void SetEnableTrue()
    {
        scriptEnabled = true;
    }

    public void SetEnableFalse()
    {
        scriptEnabled = false;
    }

    public void UnParentBrick()
    {
        // Set the parent of parentCube to null, making it its own parent again
        parentCube.transform.parent = null;

        // Optionally, make the Rigidbody kinematic false if needed
        Rigidbody parentRigidbody = parentCube.GetComponent<Rigidbody>();
        parentRigidbody.isKinematic = false;
    }
}
