import requests
import pycps
from slacker import Slacker
import json
import os

slack = Slacker('xoxp-6562741812-6562848885-6651067744-cb5f98')

from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/summarize", methods=['POST'])
def slack():
	print ("Slash command")
	return ("Vinayak good boy")

if __name__ == "__main__":
	# Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)



# response =  slack.channels.history('C06GJNJEM')

# a = (response.body)

# print (a['messages'][0]['text'])



# payload = {'apikey': secret["HP"], 'text': 'Someone I know recently combined Maple Syrup.'}

# r = requests.get('http://api.idolondemand.com/1/api/sync/extractconcepts/v1', params=payload)

# print r.text


# con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'Angel-hack', 'ketanbhatt1006@gmail.com', 'Updated@2015', '100581')

# con.insert({5: '<text>foobar</text>',
#             6: '<text>baz</text>', 
#             'id7': {'title': 'Loerem Ipsum', 'text': 'Long, long text'}})