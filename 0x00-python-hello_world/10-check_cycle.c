#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *First;
	listint_t *Second;

	First = list;
	Second = list;

	while (First != NULL && Second != NULL)
	{
		if (First->next->next == Second->next)
		{
			return (1);
		}
		First = First->next->next;
		Second = Second->next;
	}
	return (0);
}
