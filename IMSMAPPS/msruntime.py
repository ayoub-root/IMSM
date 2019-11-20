from IMSMAPPS.models import Microservices


class msruntime:
    def __init__(self):
        pass

    def __str__(self) -> str:
        return super().__str__()


    def pymicroservice(*argv, **kwargs):
        print("run service : " + str(argv[0]) + ' with option : ' + str(kwargs['args']))
        service = Microservices.objects.get(m_id=argv[1])
        print(service.cmd)