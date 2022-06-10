
from flask import Flask
from flask_restful import Api,Resource
import requests
import json
from flask import Response as r
app = Flask(__name__)
cookie = ""
api = Api(app)
password = "password"
groupid = "8593597"
url = f"https://groups.roblox.com/v1/groups/{groupid}/users/"
authurl = "https://auth.roblox.com/v2/login"
api = Api(app)
def getXsrf():
  xsrfRequest = requests.post(authurl, cookies={'.ROBLOSECURITY': cookie})
  return xsrfRequest.headers["x-csrf-token"]
    



class rank(Resource):
  def get(self,userId,rank,key):
  
   
    if key == password:
      
      requestBody = json.dumps({"roleId" : rank})
      xsrf = getXsrf()
      Response = requests.request("PATCH",
        url+userId,

        headers= {
              "Cookie": ".ROBLOSECURITY=" + cookie,
              "Content-Type": "application/json",
              "Accept": "application/json",
              "X-CSRF-TOKEN": xsrf},
        data = requestBody)
      print(Response.status_code)
      if Response.status_code == 200:
        return{
                "userId":userId,
                "rank":rank,
                "Status":Response.status_code}
      else:
        return r(status = Response.status_code)

    else:
      return r('''{acsess":"denied,
              status: incorrect key please double check what you entered or stop trying to hac D:}
                ''', status=403)
  
api.add_resource(rank,"/user/<string:userId>/rank/<string:rank>/key/<string:key>")

if __name__ == "__main__":
  app.run()
