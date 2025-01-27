import psutil
from yasmin import Blackboard
def killProcess(blackboard : Blackboard,key : str):
    try:
        if key in blackboard and blackboard.__getitem__(key):
                pid = blackboard.__getitem__(key)
                parent = psutil.Process(pid)
                children = parent.children(recursive=True) # get all sub processes

                # önce alt süreçleri kapat
                for child in children:
                    child.terminate()
                
                # ana süreci kapat
                parent.terminate()

                # pid set none
                blackboard.__setitem__(key,None)
        else:
            print(f"ERROR: there is no {key}")
    except psutil.NoSuchProcess:
        print("Süreç zaten kapanmış veya bulunamadı.")