---
layout: default
title: Home
---
{{ assign twitch_service = site.data.services | where:"name","Twitch" }}
{{ assign youtube_service = site.data.services | where:"name","YouTube" }}

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
{{ assign twitch_media_id = media.distributors | where:"name","Twitch" }}
{{ assign youtube_media_id = media.distributors | where:"name","YouTube" }}
    <tr>
      <td>{{ media.series }}</td>
      <td>{{ media.season }}</td>
      <td>{{ media.episode }}</td>
      <td>{{ media.title }}</td>
      <td>{{ media.air_date }}</td>
      <td><a href="{{ twitch_service.user_link_pattern | replace: "{media_id}",twitch_media_id }}">Twitch</a></td>
      <td><a href="{{ youtube_service.user_link_pattern | replace: "{media_id}",youtube_media_id }}">YouTube</a></td>
    </tr>
{% endfor %}
  </tbody>
</table>
