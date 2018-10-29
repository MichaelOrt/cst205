For this to work you will need to generate a client id and client secret via Spotify's developer portal.  

In the portal, you will also need to provide a redirect URI. For this example you should enter:

http://127.0.0.1:5000/

Lastly, when you run your Flask application, add the following export:

(Mac, Linux)
export OAUTHLIB_INSECURE_TRANSPORT=1

(Windows)
$env:OAUTHLIB_INSECURE_TRANSPORT = "1"
