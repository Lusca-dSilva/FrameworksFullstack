

function Enviar(){
    var nome = document.getElementById('form-nome')
    var fone = document.getElementById('form-fone')
    var email = document.getElementById('form-email')
    var obs = document.getElementById('form-obs')


    if (nome.value != '' && fone.value != '' && email.value != '' ){
        alert(`Obrigado ${nome.value} pelo envio!`)
    }
    else{
        alert('Informações faltando')
    }
    
    
}