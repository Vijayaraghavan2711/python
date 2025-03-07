<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cooking Recipes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 20px;
        }

        header h1 {
            color: #333;
        }

        .recipe-list {
            display: flex;
            justify-content: space-around;
            flex-wrap: wrap;
            gap: 20px;
        }

        .recipe-card {
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            width: 250px;
            text-align: center;
        }

        .recipe-card img {
            width: 100%;
            border-radius: 8px;
        }

        .recipe-card h3 {
            margin-top: 10px;
            color: #333;
        }

        .recipe-card p {
            color: #666;
        }

        footer {
            text-align: center;
            margin-top: 40px;
            font-size: 14px;
            color: #555;
        }
    </style>
</head>
<body>

    <header>
        <h1>Cooking Recipes</h1>
    </header>

    <div class="recipe-list">
        {% for recipe in recipes %}
            <div class="recipe-card">
                <img src="{{ recipe.image }}" alt="{{ recipe.name }}">
                <h3>{{ recipe.name }}</h3>
                <p>{{ recipe.description }}</p>
            </div>
        {% endfor %}
    </div>

    <footer>
        <p>&copy; 2025 Cooking Recipes. All rights reserved.</p>
    </footer>

</body>
</html>

