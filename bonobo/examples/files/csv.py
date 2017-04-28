import bonobo

from ._services import get_services

graph = bonobo.Graph(
    bonobo.CsvReader(path='datasets/coffeeshops.txt'),
    print,
)

if __name__ == '__main__':
    bonobo.run(graph, services=get_services())
