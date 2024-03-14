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
            elapsedTime += Time.deltaTime;

            // Verificar si ha pasado el tiempo suficiente para avanzar
            if (elapsedTime >= 1f) // Si ha pasado 1 segundo
            {
                char move = movementSequence[currentIndex];

                // Mover el carro según el próximo movimiento
                if (move == '1')
                {
                    transform.Translate(Vector3.forward * moveSpeed);
                }

                if (move == '0')
                {
                    transform.Translate(Vector3.forward * 0);
                }




                // Restablecer el tiempo acumulado y avanzar al siguiente movimiento
                elapsedTime = 0f;
                currentIndex++;
            }
        }
    }
}

