<html><meta charset='utf-8'>
	<head>
		<title>Гороскоп на сегодня</title>

		 <link rel="stylesheet" 
	                href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" 
	                integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" 
	                crossorigin="anonymous">

	     <script src="https://code.jquery.com/jquery-3.4.1.min.js"> </script>
	</head>

	<body>
		<div class="container">

			<h1>Что день {{ date }} готовит</h1>

			%if spetial_date:
			<h2>Сегодня особенный день!</h2>
			% end	
			% for pred in predicions:
			<p> {{pred}} </p>
			% end		
			
		</div>
	</body>
	<script type="text/javascript">
		console.log( {{x}});
	</script>
</html>
