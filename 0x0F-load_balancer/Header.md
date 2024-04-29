# **HTTP HEADERS**

They are key : value pairs seperated by colon, which helps in the transfer of data between a webserver and a client .

They server as communication patterns for the webserver and the client in both directions

## CLASSIFICATION OF HTTP HEADERS

#### HTTP REQUEST HEADER

    when a url is typed into the browser the browser sends a get request to the server. The http request header contains information in a text record form.

- Type, capabilities and version of the browser that generates the request.
- Operating system used by the client.
- Page that was requested.
- Various types of outputs accepted by the browser.

#### HTTP RESPONSE HEADER

when the server recieves the request, an HTTP response headers is sent back to the client, the response header contains information in a text form it includes type,date, size of the file and information regarding the webserver

#### HTTP GENERAL HEADER

Thes header contains directives to follow for both the server and client

- Caching directives.
- Specified connection options.
- The date (always listed in Greenwich Mean TIme)
- Pragma
- Upgrade (for if the protocols need to be switched)
- Via (to indicate intermediate protocols)
- Warning (for additional information not found elsewhere in the header. There may be more than one warning listed.)

#### HTTP ENTITY HEADER

These headers include information regarding:

- Allow (methods supported by the identified resource)
- Content Encoding.
- Content Language.
- Content Location.
- Content Length.
- MD-5 (for checking the integrity of the message upon receipt).
- Content Range.
- Content Type.
- When it Expires.
- When it was last modified.
