import csv
import json
import os
import random as r
import uuid
from datetime import datetime, timedelta

#region 'Account'
accountData = [
  ['248d9d75297a','Tigran Goraidh','2023-01-17T16:36:10.785014Z','MessageIdData'],
  ['6ebcb2ac944c','Vikram Sunita','2023-01-17T16:36:11.785421Z','MessageIdData'],
  ['743997192c71','Suraj Livius','2023-01-17T16:36:12.785487Z','MessageIdData'],
  ['a8d9c40ef511','Faron Domhnall','2023-01-17T16:36:13.785535Z','MessageIdData'],
  ['cd3a8437423c','Radomir Aditi','2023-01-17T16:36:14.785592Z','MessageIdData'],
  ['43510864a6f1','Katherine Ismaele','2023-01-17T16:36:15.785636Z','MessageIdData'],
  ['247263c670b8','Dolores Langston','2023-01-17T16:36:16.785678Z','MessageIdData'],
  ['fad18082a2fd','Darryl Dayton','2023-01-17T16:36:17.785719Z','MessageIdData'],
  ['280f1654a3dc','Lorayne Akicita','2023-01-17T16:36:18.785760Z','MessageIdData'],
  ['20f8aecfc69b','Deirdre Daniel','2023-01-17T16:36:19.785800Z','MessageIdData'],
  ['1dd7743b1e36','Deborah Millard','2023-01-17T16:36:20.785843Z','MessageIdData'],
  ['febda3b8e823','Itzcoatl Tex','2023-01-17T16:36:21.785883Z','MessageIdData'],
  ['3bc5a105b4cd','Rinaldo Fiorino','2023-01-17T16:36:22.785921Z','MessageIdData'],
  ['88066778efa9','Ermanno Kimimela','2023-01-17T16:36:23.785957Z','MessageIdData'],
  ['b8f896ea05af','Everett Brice','2023-01-17T16:36:24.785993Z','MessageIdData'],
  ['45f0bb6f8f16','Wilford Antonio','2023-01-17T16:36:25.786029Z','MessageIdData'],
  ['bfb248306601','Veronica Giacomina','2023-01-17T16:36:26.786066Z','MessageIdData'],
  ['ab516b7308fd','Ujarak Gerald','2023-01-17T16:36:27.786105Z','MessageIdData'],
  ['118615748df9','Shannon Maome','2023-01-17T16:36:28.786148Z','MessageIdData'],
  ['ef5ade4437d8','Fausta Enea','2023-01-17T16:36:29.78618Z7','MessageIdData']
]

def generateAccountCSV():
  path = 'timeseries/files/Account.csv'  
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','Name','TimeStamp','MessageId'])
     writer.writerows(accountData)
     file.close()
    
#endregion

#region 'Room Status'
roomStatus = [
  ['5d6ca2fb8892','N/A','2023-01-22T16:36:10.786406Z','MessageIdData'],
  ['3ee4f9210c9e','Occupied','2023-01-22T16:36:20.786454Z','MessageIdData'],
  ['a0cf264196d0','UnOccupied','2023-01-22T16:36:30.786490Z','MessageIdData'],
  ['44c43f80696a','Offline','2023-01-22T16:36:40.786525Z','MessageIdData']
]

def generateRoomStatusCSV():
  path = 'timeseries/files/RoomStatus.csv'
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','Value','TimeStamp','MessageId'])
     writer.writerows(roomStatus)
     file.close()
    
#endregion

#region 'Rooms'
rooms = [
  ['dd65c41bf379','Pax','2023-01-30T16:36:40.786406Z','MessageIdData'],
  ['9b33972d8576','Fulgora','2023-01-30T16:36:41.786406Z','MessageIdData'],
  ['8cbb2df198e2','Saturn','2023-01-30T16:36:42.786406Z','MessageIdData'],
  ['5a1febe9ed2e','Elissa','2023-01-30T16:36:43.786406Z','MessageIdData'],
  ['8cb43fec45ab','Gemini','2023-01-30T16:36:44.786406Z','MessageIdData'],
  ['0d895b175b5a','Vesta','2023-01-30T16:36:45.786406Z','MessageIdData'],
  ['d7eb2fc098ba','Luna','2023-01-30T16:36:46.786406Z','MessageIdData'],
  ['564c6b840ab5','Ceres','2023-01-30T16:36:47.786406Z','MessageIdData'],
  ['c154f41bf318','Venus','2023-01-30T16:36:48.786406Z','MessageIdData'],
  ['c4b05d20527c','Iovis','2023-01-30T16:36:49.786406Z','MessageIdData']
]

def generateRoomsCSV():
  path = 'timeseries/files/Rooms.csv'
  with open(path, 'w', encoding='UTF8', newline='') as file:
     writer = csv.writer(file)
     writer.writerow(['Cid','Value','TimeStamp','MessageId'])
     writer.writerows(rooms)
     file.close()

#endregion

#region 'RoomOccupancy'

# random.choice([0, 1])
class Room:
  def __init__(self, Cid, RoomName, StatusStart, StatusEnd, RoomHadPeople, RoomStatus, AccountCid, TimeStamp, MessageId):
    self.Cid = Cid
    self.RoomName = RoomName
    self.StatusStart = StatusStart
    self.StatusEnd = StatusEnd
    self.RoomHadPeople = RoomHadPeople
    self.RoomStatus = RoomStatus
    self.AccountCid = AccountCid
    self.TimeStamp = TimeStamp
    self.MessageId = MessageId
  
  def getDict(self):
    return vars(self)
  
  @staticmethod
  def getColumns():
    return ['Cid','RoomName','StatusStart','StatusEnd','RoomHadPeople','RoomStatus','AccountCid','TimeStamp','MessageId']


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
      headers = Room('Cid','RoomName','StatusStart','StatusEnd','RoomHadPeople','RoomStatus','AccountCid','TimeStamp','MessageId')
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
        
        data = Room(uuid.uuid4(), rooms[r.randint(0,9)][1], stStart.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), stEnd.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), roomHadPeople, roomStatus[r.randint(0,3)][1], accountData[r.randint(0,19)][0], stEnd.strftime("%Y-%m-%dT%H:%M:%S.%fZ"),'MessageIdData')
        tsSrv.addRow(data)
        
        startDate = stEnd + timedelta(minutes=minutesForRoom[r.randint(0,5)])
        
      originalDate = originalDate + timedelta(days=1)

#endregion

#region 'TimeSeries'

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
        room = rooms[r.randint(0,9)][0]
        # Start
        data = TimeSeries(room, stStart.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), roomStatus[r.randint(0,3)][1],'MessageIdData')
        tsSrv.addRow(data)
        
        # Finish
        data = TimeSeries(room, stEnd.strftime("%Y-%m-%dT%H:%M:%S.%fZ"), roomStatus[r.randint(0,3)][1],'MessageIdData')
        tsSrv.addRow(data)
        
        startDate = stEnd + timedelta(minutes=minutesForRoom[r.randint(0,5)])
        
      originalDate = originalDate + timedelta(days=1)

#endregion

#region TimeSeries JSON
class TSJson:
  def __init__(self, cid, timeStamp, accountCid, roomName, roomStartDateTime, roomEndDateTime, hasPeople, messageId, value):
    self.cid = cid
    self.timeStamp = timeStamp
    self.accountCid = accountCid
    self.roomName = roomName
    self.roomStartDateTime = roomStartDateTime
    self.roomEndDateTime = roomEndDateTime
    self.hasPeople = hasPeople
    self.messageId = messageId
    self.value = value
  
  def getDict(self):
    return vars(self)
  
  @staticmethod
  def getColumns():
    return ['cid','timeStamp','accountCid','roomName','roomStartDateTime','roomEndDateTime','hasPeople','messageId','value']


def generateTimeSeriesJSON():
  minutesForRoom = [10, 20, 30, 40, 45, 50]
  hoursForRoom = [0, 1]
  path = 'timeseries/files/RoomOccupancyStatus.json'
  originalDate = datetime.fromisoformat('2020-01-01T08:00:00')

  if os.path.exists(path):
    os.remove(path)
  
  while originalDate.date() < datetime.today().date():
    # Get the new date to generate the records
    startDate = originalDate
    
    endOfDay = False
    while endOfDay is False:
      # Avoiding Saturday and Sunday
      if startDate.isoweekday() == 6 or startDate.isoweekday() == 7:
        startDate = startDate + timedelta(days=1)
        continue
      
      if startDate.hour >= 20:
        endOfDay = True
        continue
      
      hasPeople = False if r.randint(0,6) == 6 else True
      
      # Randomly select the Hours and Minutes to be added
      hoursAdd = hoursForRoom[r.randint(0,1)]
      minutesAdd = minutesForRoom[r.randint(0,5)]
      
      stStart = startDate
      stEnd = stStart + timedelta(hours=hoursAdd) + timedelta(minutes=minutesAdd)
      
      srv = TSJson(str(uuid.uuid4()), str(stEnd.strftime("%Y-%m-%dT%H:%M:%S.%fZ")), accountData[r.randint(0,19)][0], rooms[r.randint(0,9)][1], str(stStart.strftime("%Y-%m-%dT%H:%M:%S.%fZ")), str(stEnd.strftime("%Y-%m-%dT%H:%M:%S.%fZ")), hasPeople, 'MessageIdData', roomStatus[r.randint(0,3)][1])
      
      json_data = json.dumps(srv.getDict(), indent=2)
      with open(path, 'a') as f:
        f.write(json_data+',')
        f.close()
      
      startDate = stEnd + timedelta(minutes=minutesForRoom[r.randint(0,5)])
      
    originalDate = originalDate + timedelta(days=1)
  

# endregion

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
  generateAccountCSV()
  generateRoomStatusCSV()
  generateRoomsCSV()
  generateRoomOccupancyCSV()
  generateTimeSeriesData()
  # generateTimeSeriesJSON()

#endregion