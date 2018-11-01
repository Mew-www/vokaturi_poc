# vokaturi_poc
Proof of Concept to test Vokaturi as part of Voice<=>Emotion API.

![Dataflow: Decode -> Interpret -> Serialize -> Return](https://raw.githubusercontent.com/Mew-www/vokaturi_poc/master/backend_dataflow.png)

## API logic outline:
* Receive audio via either POST or PUT method *(whichever more convenient for UI)*  
* Decode audio from Opus/VP8/Vorbis/what-ever-it-will-be to waveform (PCM)  
* Feed PCM to Vokaturi bindings  
* Receive and serialize to JSON  
* Return the JSON in HTTP response  
