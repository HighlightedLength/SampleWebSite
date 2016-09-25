@from datetime import datetime
<html>
  <head>
    <title>@model.title</title>
  </head>
  <body>
    @for p in products:
      <div>We have @p.stockCount @p.Name<div>
      <div>We @("apologize" if p.stockCount <= 0 else "hope we can help")</div>
      @if p.isNeat:
        <div>This product is really neat</div>
      @else
        <div>Really this product is bad</div>
      <div>Rendered @@ @datetime.now()</div>
  </body>
</html>
