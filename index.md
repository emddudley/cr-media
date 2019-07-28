---
layout: default
title: Home
---
# Critical Data

<table>
  <thead>
    <tr>
      <th>Series</th>
      <th>Season</th>
      <th>Episode</th>
      <th>Title</th>
      <th>Air Date</th>
    </tr>
  </thead>
  <tbody>
{% for media in site.data.media %}
    <tr>
      <td>{{ media.series }}</td>
      <td>{{ media.season }}</td>
      <td>{{ media.episode }}</td>
      <td>{{ media.title }}</td>
      <td>{{ media.air_date }}</td>
    </tr>
{% endfor %}
  </tbody>
</table>
