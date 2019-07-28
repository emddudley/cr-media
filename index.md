---
layout: default
title: Home
---
{% assign twitch_service = site.data.services | where: "name","Twitch" | first %}
{% assign youtube_service = site.data.services | where: "name","YouTube" | first %}
{% assign media_id_token = "{media_id}" %}
{% assign user_id_token = "{user_id}" %}

# Critical Data

<table>
  <thead>
    <tr>
      <th>Series</th>
      <th>Season</th>
      <th>Episode</th>
      <th>Title</th>
      <th>Air Date</th>
      <th>Twitch</th>
      <th>YouTube</th>
    </tr>
  </thead>
  <tbody>
{% for media in site.data.media %}
{% assign twitch_distribution = media.distributors | where: "name","Twitch" | first %}
{% assign youtube_distribution = media.distributors | where: "name","YouTube" | first %}
    <tr>
      <td>{{ media.series }}</td>
      <td>{{ media.season }}</td>
      <td>{{ media.episode }}</td>
      <td>{{ media.title }}</td>
      <td>{{ media.air_date }}</td>
      <td><a href="{{ twitch_service.media_link_pattern | replace: media_id_token,.twitch_distribution.media_id }}">Twitch</a></td>
      <td><a href="{{ youtube_service.media_link_pattern | replace: media_id_token,youtube_distribution.media_id }}">YouTube</a></td>
    </tr>
{% endfor %}
  </tbody>
</table>
