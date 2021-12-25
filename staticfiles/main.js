
console.log('kkll')
const socket = io('http://localhost:8000')
socket.on('connect',()=>{
                           console.log('connected')

                        })



socket.on('welcome',msg=>{
                           console.log(msg)
                            alert('created')
                        })

socket.on('welcome2',msg=>{
                           console.log(msg)
                            })