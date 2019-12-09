#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

int check_cycle(listint_t *list)
{
	listint_t *First;
	listint_t *Second;

	First = list;
	Second = list;

	while (First && Second && First->next)
	{
		First = First->next->next;
		Second = Second->next;
		if (First == Second)
		{
			return (1);
		}
	}
	return (0);
}
