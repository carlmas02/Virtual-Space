const APP_ID = '5f7dc3acd0244a25b98292f65d5d2063';

const CHANNEL  = sessionStorage.getItem('room')

const TOKEN  = sessionStorage.getItem('token')

let UID = sessionStorage.getItem('UID') ;

const client = AgoraRTC.createClient(
	{mode:'rtc',codec:'vp8'})


let localTracks = []

let remoteUsers = {}


let joinAndDisplayLocalStream  = async () => {

	console.log('host')

	document.getElementById('room-name').innerText = CHANNEL

	client.on('user-published',handleUserJoined);
	client.on('user-left',handleUserLeft)


	try{
		await client.join(APP_ID,CHANNEL,TOKEN,UID)
	}
	catch(error){
		console.log(error)
		window.open('/')
	}

	localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

	let player = `<div class = 'video-container' id = 'user-container-${UID}' >

						<div class = 'video-player' id ='user-${UID}' >
							
						</div>

				  </div>`

	document.getElementById('video-streams').insertAdjacentHTML('beforeend',player);

	localTracks[1].play(`user-${UID}`)

	await client.publish([localTracks[0],localTracks[1]])

}


let handleUserJoined = async (user,mediaType) =>{

	console.log('remote')

	remoteUsers[user.id] = user

	await client.subscribe(user,mediaType)

	if(mediaType=='video'){
		let player = document.getElementById('user-container-${user.uid}')

		if(player!=null){
			player.remove()
		}

		player = `<div class = 'video-container' id = 'user-container-${user.uid}' >

						<div class="video-player" id ='user-${user.uid}' >
							
						</div>

				  </div>`

		document.getElementById('video-streams').insertAdjacentHTML('beforeend',player);
		user.videoTrack.play(`user-${user.uid}`)

	}

	if(mediaType=='audio'){
		user.audioTrack.play()
	}

}

let handleUserLeft = async (user) =>{

	delete remoteUsers[user.uid]

	document.getElementById(`user-container-${user.uid}`).remove();


}



let leaveAndRemoveLocalStream = async () => {

	for (let i =0 ;localTracks.length>i;i++){
		localTracks[i].stop()
		localTracks[i].close()


	}

	await client.leave()

	window.open('/','_self');

}


let toggleCamera = async(e) => {
	if(localTracks[1].muted==false){
		await localTracks[1].setMuted(true)
	}
	else if(localTracks[1].muted){
		await localTracks[1].setMuted(false)
	}


}

let toggleMic = async(e) => {
	if(localTracks[0].muted==false){
		await localTracks[0].setMuted(true)
	}
	else if(localTracks[0].muted){
		await localTracks[0].setMuted(false)
	}


}


joinAndDisplayLocalStream();


leave = document.getElementById('leave')
leave.addEventListener('click',leaveAndRemoveLocalStream);

video = document.getElementById('video')
video.addEventListener('click',toggleCamera);

audio = document.getElementById('audio')
audio.addEventListener('click',toggleMic);

