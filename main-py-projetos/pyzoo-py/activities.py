from datetime import datetime


class Activity:

    def __init__(self, activityId, employeeId, activityType, description):
        self._activityId = activityId
        self._employeeId = employeeId
        self._activityType = activityType
        self._description = description
        self._timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")


    def getActivityId(self):
        return self._activityId


    def getEmployeeId(self):
        return self._employeeId


    def getActivityType(self):
        return self._activityType


    def getDescription(self):
        return self._description


    def getTimestamp(self):
        return self._timestamp


    def getActivityInfo(self):
        return {
            'id': self._activityId,
            'employee_id': self._employeeId,
            'type': self._activityType,
            'description': self._description,
            'timestamp': self._timestamp
        }


activities_dict = {}
activity_counter = 1  # Para gerar IDs únicos


def registerActivity(employeeId, activityType, description):
    global activity_counter
    
    activity_id = f"ACT{activity_counter:04d}"
    activity_counter += 1
    
    activity = Activity(activity_id, employeeId, activityType, description)
    activities_dict[activity_id] = activity
    
    return True, activity_id


def getActivity(activityId):
    return activities_dict.get(activityId, None)


def listAllActivities():
    return activities_dict


def listActivitiesByEmployee(employeeId):
    employee_activities = {}
    
    for activity_id, activity in activities_dict.items():
        if activity.getEmployeeId() == employeeId:
            employee_activities[activity_id] = activity
    
    return employee_activities


def listActivitiesByType(activityType):
    type_activities = {}
    
    for activity_id, activity in activities_dict.items():
        if activity.getActivityType() == activityType:
            type_activities[activity_id] = activity
    
    return type_activities


def getActivityCount():
    return len(activities_dict)


def getActivityCountByType(activityType):
    count = 0
    
    for activity in activities_dict.values():
        if activity.getActivityType() == activityType:
            count += 1
    
    return count
