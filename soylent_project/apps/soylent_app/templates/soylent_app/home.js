<!doctype html>
<html lang="en">
<head>

<style>
#source_list { float: left; background: red; width: 50% }
#selection_list { float: right; background: yellow; width: 50%; height: 1000px; }
</style> 

<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.5.0/jquery.min.js"></script>
<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.9/jquery-ui.min.js"></script>

<script type="text/javascript">
$( init );

function init() {
        $( "#source_list" ).sortable({connectWith: '#selection_list'});
        $( "#selection_list" ).sortable({connectWith: '#source_list'});
}
</script>

</head>
<body>

<div id="content">
    <div id="source_list">
        {% for food in foods_list %}
        <p>{{ food }}</p>
        {% endfor %}
    </div>
    <div id="selection_list">
    </div>
</div>

</body>
</html>
