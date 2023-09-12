#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
* print_python_list_info -  a C function that prints info about Python lists.
* @p: object
**/

void print_python_list_info(PyObject *p)
{
	int x;
	long int size = PyList_Size(p);
	PyListObject *object = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", object->allocated);
	for (x = 0; x < size; x++)
		printf("Element %i: %s\n", x, Py_TYPE(object->ob_item[x])->tp_name);
}
