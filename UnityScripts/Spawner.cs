using System.Collections;
using System.Globalization;
using UnityEngine;
using UnityEngine.UI;
using TMPro;

public class Spawner : MonoBehaviour
{
    public GameObject prefabToSpawn;
    public MyFloatData numberOfPrefabs;
    public TextMeshProUGUI counter;
    public Transform spawnPoint;

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
        StartCoroutine(SpawnCoroutine());
    }

    private IEnumerator SpawnCoroutine()
    {
        int numberOfInstances = Mathf.RoundToInt(numberOfPrefabs.value);

        while (numberOfInstances > 0)
        {
            Instantiate(prefabToSpawn, spawnPoint.position, Quaternion.identity);
            numberOfInstances--;

            yield return new WaitForSeconds(0.3f);
        }
    }
}
