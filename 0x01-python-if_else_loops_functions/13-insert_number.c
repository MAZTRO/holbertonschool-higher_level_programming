#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * insert_node - check the code for Holberton School students.
 * @head: Principal pointer.
 * @number: Value.
 * Return: Always 0.
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *hare = *head, *tortoise = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{return (NULL); }

	while (hare->next != NULL)
	{
		hare = hare->next;
		if (tortoise->n < number && hare->n > number)
		{
			new->n = number;
			new->next = hare;
			tortoise->next = new;
		}
		tortoise = tortoise->next;
	}
	return (new);
}
