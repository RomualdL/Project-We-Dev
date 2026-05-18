from utils import requeteJson, filterUser_list, myFormatData


MY_API = "https://jsonplaceholder.typicode.com/users"

def main(MY_API):
    rq_json = requeteJson(MY_API)
    user = filterUser_list(rq_json)
    return myFormatData(user)

if __name__ == "__main__":
    print(main(MY_API))