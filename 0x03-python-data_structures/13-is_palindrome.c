#include "lists.h"

/**
 * get_nodeint_at_index - writes the character c to stdout
 * @head: The character to print
 * @index: lol
 * Return: list
 */

listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	unsigned int count = 0;
	listint_t *cpy;

	if (head != NULL)
	{
		cpy = head;

		while (cpy != NULL)
		{
			if (count == index)
			{
				return (cpy);
			}
			cpy = (*cpy).next;
			count++;
		}
	}
	return (NULL);
}

/**
 * *add_nodeint - writes the character c to stdout
 * @head: The character to print
 * @n: number
 * Return: list
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *cpy;

	cpy = malloc(sizeof(listint_t));
	if (cpy == NULL)
	{
		return (NULL);
	}
	cpy->n = n;
	cpy->next = *head;
	*head = cpy;

	return (cpy);
}

/**
 * free_listint2 - Free all nodes
 * @head: the list
 * Return: Nothing
 */

void free_listint2(listint_t **head)
{
	listint_t *cpy = NULL;

	if (head == NULL)
	{
		return;
	}

	cpy = *head;

	while (*head != NULL)
	{
		cpy = (*cpy).next;
		free(*head);
		*head = cpy;
	}
	head = NULL;
}

/**
 * is_palindrome - Test if is a palindrome
 * @head: The character to test
 * Return: 1 if is palindrome, otherwise 0
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp;
    int count = 0, len = 0;

    if (head != NULL || *head != NULL)
    {
        while (*head != NULL)
        {
            count++;
            *head = (**head).next;
        }
        if (count % 2 == 0)
        {
            count = count / 2;
            add_nodeint(get_nodeint_at_index(*head, count))
        }
    }
}
