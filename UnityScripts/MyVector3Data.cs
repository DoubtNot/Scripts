using UnityEngine;

[CreateAssetMenu]

public class MyVector3Data : ScriptableObject
{

    public Vector3 value;

    public void SetValue(Vector3 v3)
    {
        value = v3;
    }

    public void SetValue(Transform t)
    {
        value = t.position;
    }

    public void SetTransform(Transform t)
    {
        t.position = value;
    }


}
