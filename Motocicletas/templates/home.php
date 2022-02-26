<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>inicio</title>
</head>
<style>
  .abs-center {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

.table {
  width: 450px;
}
.table-hover tbody tr:hover {
      background-color: rgba(122, 114, 81, 0.7);
      color: rgb(112, 24, 78);
    }

</style>
<body>
  <h2>Cantidad de motocicletas restantes: <div id="cantMotos" >{{cant_motos}} </div></h2>
    <div class="container-lg">
      <script>var horas = [];</script>
      <div class="abs-center">
        <table class="table" class="border p-3 table" >
              {% for h in lineas %}
              <div>
                <tr  id="{{h}}">              
                  <th scope="col" onclick="controlMotos({{h}})">
                    {{h}} hs
                  </th>
                  <script> horas[{{h}}]=1</script>                
                </tr>
              </div>
              {% endfor %}
              
          </table>
      </div>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </div>
  <script>
    
    function controlMotos(id){
      var textContent = document.getElementById('cantMotos'),
      texto = textContent.textContent;

      if (horas[id]== 0 ){
        document.getElementById('cantMotos').innerHTML = Number(texto)+1;
        horas[id]= 1;                
        document.getElementById(id).style.backgroundColor = 'white'
      }
      else if (Number(texto) ==0 && horas[id]== 1){
        alert("No hay mas motos disponibles");

      }
      else if (Number(texto) > 0 && horas[id]== 1){
        document.getElementById('cantMotos').innerHTML = Number(texto)-1;
        horas[id]= 0;
        document.getElementById(id).style.backgroundColor = 'red'
      }
      

    }
  
  </script>
</body>
</html>