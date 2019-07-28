---
layout: default
title: Home
---
# Critical Data

<table>
  <thead>
    <tr>
      <th>Series</th>
      <th>Episode</th>
      <th>Title</th>
    </tr>
  </thead>
  <tbody>
    <tr>
{% for media in site.data.episodes[media] %}
      <td>{{ media.title }}</td>
{% endfor %}
    </tr>
  </tbody>
</table>
