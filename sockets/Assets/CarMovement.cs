using UnityEngine;

public class CarMovement : MonoBehaviour
{
    // Variables públicas para almacenar la información del carro
    public string direction;
    public string initialPosition;
    public string movementSequence;

    public float moveSpeed = 1f; // Velocidad de movimiento del carro en metros por segundo
    //private string movementSequence; // Secuencia de movimientos del carro
    private int currentIndex = 0; // Índice actual en la secuencia

    private float elapsedTime = 0f;
    //private float timeBetweenMoves = 1f / 60f; // Tiempo entre movimientos para cumplir con aproximadamente 60 fps
private Vector3 targetPosition; // Posición objetivo del próximo movimiento
    // Método para establecer la secuencia de movimientos del carro
    public void SetMovementSequence(string sequence)
    {
        movementSequence = sequence;
    }

    public void SetInitialPosition(string sequence)
    {
        initialPosition = sequence;
    }

    public void SetDirection(string sequence)
    {
        direction = sequence;
    }

    public void Update()
    {
        if (movementSequence != null && currentIndex < movementSequence.Length)
        {
            // Obtener el próximo carácter de la secuencia de movimiento
            char move = movementSequence[currentIndex];

            // Calcular la posición objetivo del próximo movimiento
            targetPosition = transform.position + (move == '1' ? Vector3.forward : Vector3.zero);

            // Interpolar suavemente entre la posición actual y la posición objetivo
            transform.position = Vector3.Lerp(transform.position, targetPosition, moveSpeed * Time.deltaTime);

            // Verificar si la posición actual está lo suficientemente cerca de la posición objetivo
            if (Vector3.Distance(transform.position, targetPosition) < 0.01f)
            {
                // Avanzar al siguiente movimiento
                currentIndex++;
            }
        }
    }
}



