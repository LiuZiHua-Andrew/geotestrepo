import os
import sys
import uuid
import json
import subprocess

#s3_client = boto3.client('s3')

try:  
    # cmd = f"ogr2ogr -f CSV -dialect sqlite -sql 'SELECT ST_X(ST_Centroid(ST_Transform(geometry, 4326))) AS Long, ST_Y(ST_Centroid(ST_Transform(geometry, 4326))) AS Lat, * FROM AU_Buildings' outputt.csv AU_Buildings.json"
    # os.system(cmd)
    subprocess.run(["ogr2ogsr","-f","geojson","-t_srs","epsg:4326","outputexception.geojon","AU_Buildings.json"])
except Exception as e:        
    print(e)
    print("Here is the error catch block")

def lambda_handler(event, context):
    bucketname="lambda-test-andrew"
    inputfilename="AU_Buildings.json"
    outputfilePath="/tmp/output.json"
    convertedfilePath="/tmp/converted.csv"
    uploadfilename="converted.geojson"
    
    # s3_client.download_file(bucketname,inputfilename,outputfilePath)
    
    # ogr2ogr.main(["","-f","geojson","-t_srs","EPSG:4326",convertedfilePath,outputfilePath])
    
    # f = open(convertedfilePath)
    # print(json.load(f))
    
    # response = s3_client.upload_file(convertedfilePath, bucketname,uploadfilename)
    # print(response)
    #cmd="cd /opt/lib && ls"
    
    #cmd = f"/opt/bin/ogr2ogr -f CSV -dialect sqlite -sql 'SELECT ST_X(ST_Centroid(ST_Transform(geometry, 4326))) AS Long, ST_Y(ST_Centroid(ST_Transform(geometry, 4326))) AS Lat, * FROM outputt' outputt.csv AU_Buildings.json"
    #os.system(cmd)
    
