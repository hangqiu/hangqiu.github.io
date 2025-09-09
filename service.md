---
layout: page
title: Service
---
#### Organizing Committee

{% assign all_service = site.data.service | sort: "year" | reverse %}
<ul>
  {% assign seen_series = "" | split: "" %}
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "oc" %}
      {% unless seen_series contains item.series %}
        {% assign seen_series = seen_series | push: item.series %}
        <li>{{ item.venue }} ({{ item.series }})
          {% assign years = "" | split: "" %}
          {% for oc in all_service %}
            {% if oc.ENTRYTYPE == "oc" and oc.series == item.series %}
              {% unless years contains oc.year %}
                {% assign years = years | push: oc.year | sort %}
              {% endunless %}
            {% endif %}
          {% endfor %}
          {{ years | join: ", " }}
        </li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>


<!-- * ACM International Conference on Mobile Systems, Applications, and Services (MobiSys'25)
* ACM Conference on Embedded Networked Sensor Systems (SenSys'25)
* ACM International Workshop on Mobile Computing Systems and Applications (HotMobile'25) -->

#### Technical Program Committee

<ul>
  {% assign seen_series = "" | split: "" %}
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "tpc" %}
      {% unless seen_series contains item.series %}
        {% assign seen_series = seen_series | push: item.series %}
        <li>{{ item.venue }} ({{ item.series }})
          {% assign years = "" | split: "" %}
          {% for oc in all_service %}
            {% if oc.ENTRYTYPE == "tpc" and oc.series == item.series %}
              {% unless years contains oc.year %}
                {% assign years = years | push: oc.year | sort %}
              {% endunless %}
            {% endif %}
          {% endfor %}
          {{ years | join: ", " }}
        </li>
      {% endunless %}
    {% endif %}
  {% endfor %}
</ul>


<!-- * ACM International Conference on Mobile Systems, Applications, and Services (MobiSys’23,'24,'25)
* ACM International Conference on Mobile Computing and Networking (MobiCom'25,'26)
* ACM Conference on Embedded Networked Sensor Systems (SenSys'25)
* USENIX Symposium on Networked Systems Design and Implementation (NSDI'25)
* IEEE Conference on Computer Communications (INFOCOM’24,'25)
* NDSS Symposium on Vehicle Security and Privacy (NDSS VehicleSec'24,'25)
* IEEE International Conference on Parallel and Distributed Systems (ICPADS’22)
* USENIX Symposium on Vehicle Security and Privacy (VehicleSec'25) -->

#### Conference Reviewer
{% assign all_service = site.data.service %}
<ul>
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "reviewer" and item.keywords contains "conf" %}
        <li>{{ item.venue }} ({{ item.series }})</li>
    {% endif %}
  {% endfor %}
</ul>

<!-- * IEEE/CVF Computer Vision and Pattern Recognition Conference (CVPR)
* IEEE/CVF International Conference on Computer Vision (ICCV)
* European Conference on Computer Vision (ECCV)
* Conference on Robot Learning (CoRL)
* IEEE International Conference on Robotics and Automation (ICRA)
* AAAI Conference on Artificial Intelligence (AAAI)
* International Conference for High Performance Computing, Networking, Storage, and Analysis (SC)
* ACM International Conference on Measurement and Modeling of Computer Systems (SIGMETRICS)
* ACM/IEEE Symposium on Edge Computing (SEC)
* ACM International Conference on Information Processing in Sensor Networks (IPSN)
* IEEE International Conference on Sensing, Communication and Networking (SECON)
* IEEE Vehicular Networking Conference (VNC)
* IEEE International Conference on Parallel and Distributed Systems (ICPADS) -->


#### Journal Reviewer

<ul>
  {% for item in all_service %}
    {% if item.ENTRYTYPE == "reviewer" and item.keywords contains "journal" %}
        <li>{{ item.venue }} ({{ item.series }})</li>
    {% endif %}
  {% endfor %}
</ul>

<!-- * IEEE Transactions on Networking (TON)
* IEEE Journal on Selected Areas in Communications (JSAC)
* IEEE Network Magazine
* IEEE Robotics and Automation Letters (RA-L)
* IEEE Transactions on Vehicular Technology (TVT)
* IEEE Transactions on Mobile Computing (TMC)
* IEEE Access
* IEEE Transactions on Cloud Computing (TCC)
* IEEE Transactions on Intelligent Transportation Systems (T-ITS)
* IEEE Internet of Things Journal (IoT-J)
* IEEE Vehicular Technology Magazine (VTM) -->

#### ACM SIGMOBILE YouTube Channel
* HotMobile’17, Mobicom’16, Mobihoc’16, Sensys’16
