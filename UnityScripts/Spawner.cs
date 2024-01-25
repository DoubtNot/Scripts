using System.Globalization;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Spawner : MonoBehaviour
{
    public GameObject prefabToSpawn; // Reference to the prefab you want to spawn
    public MyFloatData numberOfPrefabs; // The number of prefabs to spawn
    public TextMeshProUGUI counter;
    public Transform spawnPoint; // The spawn point for the prefabs


    private void Start()
    {
        counter = GetComponent<TextMeshProUGUI>();
        UpdateCounter();
    }

    public void UpdateCounter()
    {
        counter.text = numberOfPrefabs.value.ToString(CultureInfo.InvariantCulture);
    }

    public void SpawnPrefabs()
    {
        int numberOfInstances = Mathf.RoundToInt(numberOfPrefabs.value);

        while (numberOfInstances > 0)
        {
            Instantiate(prefabToSpawn, spawnPoint.position, Quaternion.identity);
            // You can adjust the spawn rotation as needed.

            numberOfInstances--;
        }
    }

}
