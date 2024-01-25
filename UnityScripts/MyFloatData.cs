using UnityEngine;

[CreateAssetMenu]
public class MyFloatData : ScriptableObject
{
    public float value;

    public void UpdateValue(float num)
    {
        value += num;
    }

    public void SetValue(float newValue)
    {
        value = newValue;
    }

}
