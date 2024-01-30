using UnityEngine;
using UnityEngine.Events;

public class MatchBehavior : MonoBehaviour
{

    public ID idObj;
    public UnityEvent matchEvent, noMatchEvent;

    public bool scriptEnabled = false;

    private void OnTriggerEnter(Collider other)
    {
        var tempID = other.GetComponent<IDContainerBehavior>();
        if (tempID == null)
            return;

        var otherID = tempID.idObj;
        if (otherID == idObj && scriptEnabled)
        {
            matchEvent.Invoke();
        }
        else
        {
            noMatchEvent.Invoke();
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

}
