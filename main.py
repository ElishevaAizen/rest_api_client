from rest_api_client import RestAPIClient

def main():
  url="https://resttest10.herokuapp.com"
  
  #create an instace for rest_api_client object
  rest_api_client=RestAPIClient(url)
  
  ####Task_1####
  #get response for serial 1
  response_1=rest_api_client.get_replay(1)
  print(response_1)
  #get response for serial 2
  response_2=rest_api_client.get_replay(2)
  print(response_2)
  
  ####Task_2####
  #get data for posting request
  data=RESTAPIClient.get_data(response_1,response_2)
  #send the data for posting request
  response=rest_api_client.send_request(data)
  #check if posting is done successfully
  assert(response.ok)
  print ("correct")
  
  if __name__ == "__main__":
  main()
