import csv
import os
import random as r
import uuid
from datetime import datetime, timedelta

#region 'Account'
accountData = [
  ['248d9d75297a','Tigran Goraidh','2023-01-17 16:36:10.785014'],
  ['6ebcb2ac944c','Vikram Sunita','2023-01-17 16:36:11.785421'],
  ['743997192c71','Suraj Livius','2023-01-17 16:36:12.785487'],
  ['a8d9c40ef511','Faron Domhnall','2023-01-17 16:36:13.785535'],
  ['cd3a8437423c','Radomir Aditi','2023-01-17 16:36:14.785592'],
  ['43510864a6f1','Katherine Ismaele','2023-01-17 16:36:15.785636'],
  ['247263c670b8','Dolores Langston','2023-01-17 16:36:16.785678'],
  ['fad18082a2fd','Darryl Dayton','2023-01-17 16:36:17.785719'],
  ['280f1654a3dc','Lorayne Akicita','2023-01-17 16:36:18.785760'],
  ['20f8aecfc69b','Deirdre Daniel','2023-01-17 16:36:19.785800'],
  ['1dd7743b1e36','Deborah Millard','2023-01-17 16:36:20.785843'],
  ['febda3b8e823','Itzcoatl Tex','2023-01-17 16:36:21.785883'],
  ['3bc5a105b4cd','Rinaldo Fiorino','2023-01-17 16:36:22.785921'],
  ['88066778efa9','Ermanno Kimimela','2023-01-17 16:36:23.785957'],
  ['b8f896ea05af','Everett Brice','2023-01-17 16:36:24.785993'],
  ['45f0bb6f8f16','Wilford Antonio','2023-01-17 16:36:25.786029'],
  ['bfb248306601','Veronica Giacomina','2023-01-17 16:36:26.786066'],
  ['ab516b7308fd','Ujarak Gerald','2023-01-17 16:36:27.786105'],
  ['118615748df9','Shannon Maome','2023-01-17 16:36:28.786148'],
  ['ef5ade4437d8','Fausta Enea','2023-01-17 16:36:29.786187']
]

def generateAccountCSV():
  path = 'timeseries/files/Account.csv'  
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','Name','TimeStamp'])
     writer.writerows(accountData)
     file.close()
    
#endregion

#region 'Room Status'
roomStatus = [
  ['5d6ca2fb8892','N/A','2023-01-22 16:36:10.786406'],
  ['3ee4f9210c9e','Occupied','2023-01-22 16:36:20.786454'],
  ['a0cf264196d0','UnOccupied','2023-01-22 16:36:30.786490'],
  ['44c43f80696a','Offline','2023-01-22 16:36:40.786525']
]

def generateRoomStatusCSV():
  path = 'timeseries/files/RoomStatus.csv'
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','RoomStatus','TimeStamp'])
     writer.writerows(roomStatus)
     file.close()
    
#endregion

#region 'Rooms'
rooms = [
  ['dd65c41bf379','Pax','2023-01-30 16:36:40.786406'],
  ['9b33972d8576','Fulgora','2023-01-30 16:36:41.786406'],
  ['8cbb2df198e2','Saturn','2023-01-30 16:36:42.786406'],
  ['5a1febe9ed2e','Elissa','2023-01-30 16:36:43.786406'],
  ['8cb43fec45ab','Gemini','2023-01-30 16:36:44.786406'],
  ['0d895b175b5a','Vesta','2023-01-30 16:36:45.786406'],
  ['d7eb2fc098ba','Luna','2023-01-30 16:36:46.786406'],
  ['564c6b840ab5','Ceres','2023-01-30 16:36:47.786406'],
  ['c154f41bf318','Venus','2023-01-30 16:36:48.786406'],
  ['c4b05d20527c','Iovis','2023-01-30 16:36:49.786406']
]

def generateRoomsCSV():
  path = 'timeseries/files/Rooms.csv'
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','RoomName','TimeStamp'])
     writer.writerows(rooms)
     file.close()

#endregion

#region 'RoomOccupancy'

# random.choice([0, 1])
class Room:
  def __init__(self, Cid, RoomName, StatusStart, StatusEnd, RoomHadPeople, RoomStatus, AccountCid, TimeStamp):
    self.Cid = Cid
    self.RoomName = RoomName
    self.StatusStart = StatusStart
    self.StatusEnd = StatusEnd
    self.RoomHadPeople = RoomHadPeople
    self.RoomStatus = RoomStatus
    self.AccountCid = AccountCid
    self.TimeStamp = TimeStamp
  
  def getDict(self):
    return vars(self)
  
  @staticmethod
  def getColumns():
    return ['Cid','RoomName','StatusStart','StatusEnd','RoomHadPeople','RoomStatus','AccountCid','TimeStamp']


def generateRoomOccupancyCSV():
  minutesForRoom = [10, 20, 30, 40, 45, 50]
  hoursForRoom = [0, 1]
  path = 'timeseries/files/RoomOccupancy.csv'
  originalDate = datetime.fromisoformat('2017-01-01T08:00:00.123456')
  firstRecord = True

  if os.path.exists(path):
    os.remove(path)
    
  tsSrv = TimeSeriesService(path, Room.getColumns())
  
  while originalDate.date() < datetime.today().date():
    # Get the new date to generate the records
    startDate = originalDate
    
    if firstRecord is True:
      headers = Room('Cid','RoomName','StatusStart','StatusEnd','RoomHadPeople','RoomStatus','AccountCid','TimeStamp')
      tsSrv.addRow(headers)
      firstRecord = False
    elif firstRecord is False:
      endOfDay = False
      
      while endOfDay is False:
        # Avoiding Saturday and Sunday
        if startDate.isoweekday() == 6 or startDate.isoweekday() == 7:
          startDate = startDate + timedelta(days=1)
          continue
        
        if startDate.hour >= 20:
          endOfDay = True
          continue
        
        roomHadPeople = False if r.randint(0,6) == 6 else True
        
        # Randomly select the Hours and Minutes to be added
        hoursAdd = hoursForRoom[r.randint(0,1)]
        minutesAdd = minutesForRoom[r.randint(0,5)]
        
        stStart = startDate
        stEnd = stStart + timedelta(hours=hoursAdd) + timedelta(minutes=minutesAdd)
        
        data = Room(uuid.uuid4(), rooms[r.randint(0,9)][1], stStart, stEnd, roomHadPeople, 
                  roomStatus[r.randint(0,3)][1], accountData[r.randint(0,19)][0], stEnd)
        tsSrv.addRow(data)
        
        startDate = stEnd + timedelta(minutes=minutesForRoom[r.randint(0,5)])
        
      originalDate = originalDate + timedelta(days=1)

#endregion

#region 'RoomOccupancy'

# random.choice([0, 1])
class TimeSeries:
  def __init__(self, Cid, TimeStamp, Value, MessageId):
    self.Cid = Cid
    self.TimeStamp = TimeStamp
    self.Value = Value
    self.MessageId = MessageId
  
  def getDict(self):
    return vars(self)
  
  @staticmethod
  def getColumns():
    return ['Cid','TimeStamp','Value','MessageId']


def generateTimeSeriesData():
  minutesForRoom = [10, 20, 30, 40, 45, 50]
  hoursForRoom = [0, 1]
  path = 'timeseries/files/TimeSeries.csv'
  originalDate = datetime.fromisoformat('2017-01-01T08:00:00.123456')
  firstRecord = True

  if os.path.exists(path):
    os.remove(path)
    
  tsSrv = TimeSeriesService(path, TimeSeries.getColumns())
  
  while originalDate.date() < datetime.today().date():
    # Get the new date to generate the records
    startDate = originalDate
    
    if firstRecord is True:
      headers = TimeSeries('Cid','TimeStamp','Value','MessageId')
      tsSrv.addRow(headers)
      firstRecord = False
    elif firstRecord is False:
      endOfDay = False
      
      while endOfDay is False:
        # Avoiding Saturday and Sunday
        if startDate.isoweekday() == 6 or startDate.isoweekday() == 7:
          startDate = startDate + timedelta(days=1)
          continue
        
        if startDate.hour >= 20:
          endOfDay = True
          continue
        
        # Randomly select the Hours and Minutes to be added
        hoursAdd = hoursForRoom[r.randint(0,1)]
        minutesAdd = minutesForRoom[r.randint(0,5)]
        
        stStart = startDate
        stEnd = stStart + timedelta(hours=hoursAdd) + timedelta(minutes=minutesAdd)
        
        # Start
        data = TimeSeries(uuid.uuid4(), stStart, roomStatus[r.randint(0,3)][1],'')
        tsSrv.addRow(data)
        
        # Finish
        data = TimeSeries(uuid.uuid4(), stEnd, roomStatus[r.randint(0,3)][1],'')
        tsSrv.addRow(data)
        
        startDate = stEnd + timedelta(minutes=minutesForRoom[r.randint(0,5)])
        
      originalDate = originalDate + timedelta(days=1)

#endregion

#region 'General'

class TimeSeriesService:
  def __init__(self, fp, columns):
    self.filePath = fp
    self.columns = columns
    
  def addRow(self, srv):
    with open(self.filePath, 'a', encoding='UTF8', newline='') as file:
      writer = csv.DictWriter(file, fieldnames=self.columns)
      writer.writerow(srv.getDict())
      file.close()


#endregion

#region 'Main'
if __name__ == '__main__':
  # generateAccountCSV()
  # generateRoomStatusCSV()
  # generateRoomsCSV()
  # generateRoomOccupancyCSV()
  generateTimeSeriesData()

#endregion