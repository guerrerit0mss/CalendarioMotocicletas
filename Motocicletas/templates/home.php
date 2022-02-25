<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <title>inicio</title>
</head>
<body>
  <h2>Cantidad de motocicletas restantes: <div id="cantMotos" >{{cant_motos}} </div></h2>
    <div class="container-lg">
      <script>var horas = [];</script>
      <table class="table">
            {% for h in lineas %}
            <tr>
              
              <th scope="col"><a onclick="restar({{h}})">{{h}}</th>
              <script> horas[{{h}}]=0</script>
                
            </tr>
            {% endfor %}
            
        </table>
        <script>alert(horas);</script>
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </div>
  <script>
    function aumentar(){
      var textContent = document.getElementById('cantMotos'),
      texto = textContent.textContent;
      document.getElementById('cantMotos').innerHTML = Number(texto)+1;
    }
    function restar(id){
      var textContent = document.getElementById('cantMotos'),
      texto = textContent.textContent;
      document.getElementById('cantMotos').innerHTML = Number(texto)-1;
      document.getElementById('cantMotos').innerHTML = id;
    }
    restar();
  
  </script>
</body>
</html>