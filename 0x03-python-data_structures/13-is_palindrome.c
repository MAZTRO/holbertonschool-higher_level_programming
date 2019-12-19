#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: Head of a list
 * Return: 1 if the list is a palindrome, else return 0.
 */

int is_palindrome(listint_t **head)
{
	listint_t *bef = *head, *aft = *head;
	listint_t *current, *prev = NULL;
	int test = 0;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (aft != NULL && aft->next != NULL)
		{
			aft = aft->next->next;
			bef = bef->next;
		}
		current = bef;
		while (current != NULL)
		{
			aft = current->next;
			current->next = prev;
			prev = current;
			current = aft;
		}
		aft = *head;
		current = prev;
		while (prev != NULL)
		{
			if (aft->n != prev->n)
			{
				return (test);
			}
			aft = aft->next;
			prev = prev->next;
		}
	}
	return (1);
}
