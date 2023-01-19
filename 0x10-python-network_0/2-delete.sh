#!/bin/bash                                                                                                                                     
# sends a DEL URL req passed as the 1st arg and displays response body                                                                          
curl - s "$1" - X DELETE
