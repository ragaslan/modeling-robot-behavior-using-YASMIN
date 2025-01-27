from yasmin import Blackboard,State

class TaskListenerState(State):
    def __init__(self):
        super().__init__(["task_accepted"])
    
    def show_menu(self,stations):
        print("*******************\n")
        print("Stations: \n")
        
        for i in range(len(stations)):
            print(f" Station {i}\n")
        print("*******************\n")

        print("GIVE COMMAND TO ROBOT\n")

        # 1 noktaya gitme görevleri için
        print(" 1) Hedefe Git")
        print(" 2) Hedefe Sırayla Git")
        print(" 3) Hedefler Arası Tekrarlı Git")


    def execute(self,blackboard : Blackboard) -> str:
        print("***********")
        # burada bir dinleme mekanizması olmalı seçim ekran ya da
        # istasyon bilgilerini versin ve görevler gözüksün
        ## istasyon bilgileri
        stations = []
        # dosyayı okuma 
        stations_file = open("stations.txt","r")
        while True:
            content = stations_file.readline().rstrip("\n")
            if not content:
                break
            arr = content.split(',')
            
            station = dict()

            for arr_item in arr:
                # key değeri ile x,y,z 
                # value ile bu x,y,z ye karşılık gelen değer alınır
                key = arr_item.split(":")[0]
                value = arr_item.split(":")[1]
                station[key] = value
            
            stations.append(station)

        blackboard["charge_station"] = stations[0]

        # menu goster ve input al
        while True:
            self.show_menu(stations)
            print("Select command: ")
            choice = input()
            # verilen inputa blackboard a görev tanımla
            if choice == "1":
                ### burada istasyon girdisini kontrol et UYGULAMA PATLIYOR BURDA
                print("Which station you want to go ? ")
                station_choice = input()
                blackboard["mission"] = dict()
                blackboard["mission"]["type"] = 1
                blackboard["mission"]["target"] = stations[int(station_choice)]
                #print(blackboard["mission"])
                break
            if choice == "2":
                print("Hedef istasyonlari bosluk birakarak sirasiyla gir: ")
                stationsChoice = input()
                target_stations = stationsChoice.split(" ")
                blackboard["mission"] = dict()
                blackboard["mission"]["type"] = 2
                mission_target = []
                for target_station in target_stations:
                    mission_target.append(stations[int(target_station)])
                blackboard["mission"]["target"] = mission_target
                break
            if choice == "3":
                print("Tekrarli gorev yapmak istedigin istasyonlari bosluk birakarak gir: ")
                stationsChoice = input()
                target_stations = stationsChoice.split(" ")
                blackboard["mission"] = dict()
                blackboard["mission"]["type"] = 3
                mission_target = []
                for target_station in target_stations:
                    mission_target.append(stations[int(target_station)])
                print("\nLutfen tekrar sayisini giriniz: ")
                loop_count = int(input())
                
                mission_with_loop = []
                
                prev_pos = 1

                for i in range(loop_count):
                    if(prev_pos == 1):
                        mission_with_loop.append(mission_target[0])
                        prev_pos = 0
                    else:
                        mission_with_loop.append(mission_target[1])
                        prev_pos = 1    

                blackboard["mission"]["target"] = mission_with_loop
                print(mission_with_loop)
                break

        # yapılması için navigasyon durumuna geçiş yap
        return "task_accepted"