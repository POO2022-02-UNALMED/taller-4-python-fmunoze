
class Grupo:

    grado = 12

    def __init__(self, grupo="grupo ordinado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        if self._asignaturas is None:
            self._asignaturas = []
        for x in kwargs:
            self._asignaturas.append(x)

    def agregarAlumno(self, alumno, lista=None):
        if self.listadoAlumnos is None:
            self.listadoAlumnos = []
        if lista is None:
            self.listadoAlumnos.append(alumno)
        else:
            self.listadoAlumnos = lista + [alumno]

    def __str__(self):
        return f"Grupo de estudiantes: {self._grupo}"

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre