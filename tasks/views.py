from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request

from tasks.services.json_util import read_json, write_json
USERS="users.json"
TASKS="tasks.json"


@api_view(["GET"])
def users(request:Request)->Response:
    users=read_json(USERS)
    return Response(data=users, status=status.HTTP_200_OK)


@api_view(["GET"])
def user_detail(request: Request, user_id:int)->Response:
    users= read_json(USERS)

    user=None
    for i in users:
        if(i["id"]==user_id):
            user=i
            break

    if user is None:
        return Response({"error":f"user with id:{user_id} was not"},
        status=status.HTTP_404_NOT_FOUND,)

    return Response(user)

# creat6e a new user
@api_view(["POST"])
def create_user(request:Request)->Response:
    users=read_json(USERS)

    username=request.data.get("userName")
    email=request.data.get("email")

    if not username or not email:
        return Response(
            {"errors":"username and email are required fields"},
            status=status.status.HTTP_400_BAD_REQUEST,
        )
    
    #we used set why because fetching is very easy from set and set is unique
    user_name_set:set[str]=set[str]()
    email_set:set[str]=set[str]()

    max_id=0
    for u in users:
        max_id=max(max_id, u["id"])
        user_name_set.add(u["userName"])
        email_set.add(u["email"])
    
    if username in users:
        return Response({"error":f"{username} is already taken"},
        status=status.HTTP_400_BAD_REQUEST
        )
    
    new_id=max_id+1

    user={
        "id":new_id,
        "username":username,
        "email":email
    }

    users.append(user)

    write_json(USERS, users)

    return Response(user, status=status.HTTP_201_CREATED)