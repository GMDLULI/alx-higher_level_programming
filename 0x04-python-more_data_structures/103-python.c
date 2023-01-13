#include <stdio.h>
#include <Python.h>

/**
  * print-python_bytes- Prints bytes information
  *
  * @p: return object
  * Return :no return
  */

void print_python_bytes(Pyobject *p)
{
	char *string;
	long int size, i limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_check(P))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)(P))->ob_size;
	string = ((Pybytesobject *)p)->ob_sval;

	printf("  size: %d\n", size);
	printf("  trying string: %s\n", string);

	if (size >= 10)
		limit = 10;
	else
		limit = size + 1;

	printf("  first %d bytes:", limit);

	for (i = 0; i < limit; i++)
		if (string[i] >= 0)
			printf("  %02x", string[i]);
		else 
			printf(" %02x", 256 + string[i]);
	printf("\n");
}

/**
  * print_python_list - Prints list information
  *
  * @p: Python Object
  * Return : no return
  */
void print_python_list(PyVarObject *p)
{
	long int size, i;
	PylistObject *list;
	PyObject *obj;

	size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python list + %ld\n", size);
	printf("[*] Alloctaed = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		obj = ((PyListObject *)p)->Ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}


