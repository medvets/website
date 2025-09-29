title: Aktueller Notdienst für Klein- und Heimtiere 


 Während der regulären Arbeitszeiten oder auch bei Notfällen an Werktagen in der Zeit von 8:00 Uhr bis 18:00 Uhr können Sie sich eine Praxis im Menüpunkt [Praxen und Kliniken](tieraerzte.html) aussuchen. In diesem Zeitraum sind immer Tierarztpraxen im Kreis erreichbar. 
 Bitte prüfen Sie zunächst, ob der Tierarzt Ihres Vertrauens erreichbar ist und sich um Ihren Liebling kümmern kann.
In den Notdienstzeiten haben Sie zusätzlich die Möglichkeit die unten genannte notdiensthabende Praxis zu kontaktieren.

Als Notdienstzeit gilt wochentags die Zeit von 18:00 Uhr bis zu einem darauffolgenden Werktag um 8:00 Uhr. (an Feiertagen gilt dies entsprechend).

An Wochenenden beginnt der Notdienst am Freitag um 18:00 Uhr und dauert bis zum darauffolgenden Montag um 8:00 Uhr.

Falls Sie während der Notdienstzeiten eine Behandlung wünschen bedenken Sie bitte, dass die Vergütung im Notdienst entsprechend § 3 (4) der GOT erfolgt: "Einfache Gebührensätze nach Absatz 1 erhöhen sich um 100 vom Hundert, ...für Leistungen, die auf Verlangen des Tierbesitzers bei **Nacht** ..., an **Wochenenden** ... und an **Feiertagen** erbracht werden."

Die Tierärzte sind verpflichtet, **mindestens den 2fachen Gebührensatz** zu verlangen. 
Zusätzlich ist eine **Notdienstgebühr von 50,- €** (zzgl. Mwst.) pro Behandlungsfall zu erheben. 

Bitte haben Sie Verständnis dafür, dass insbesondere in den Notdienstzeiten keine telefonische Beratung stattfinden kann. Lediglich eine vorherige telefonische Anmeldung ist dringend erforderlich, damit Ihr Notfall auch zeitnah behandelt werden kann. Erst durch die Vorstellung und Untersuchung in der Praxis kann der entsprechende Fall vom Tierarzt fachgerecht beurteilt werden.

Nachfolgend wird die notdiensthabende Praxis angezeigt. 

<!-- Anleitung: In Klammern nach der Praxis-Überschrift eine Komma-getrennte Liste der Daten oder Datumsbereiche.
Ein Datum wird in der Form TT.MM.JJJJ angegeben und ein Datumsbereich als TT.MM.JJJJ-TT.MM.JJJJ
Automatisch wird der Notdienst 12 Stunden vorher und 8 Stunden nachher noch angezeigt. -->


[Praxis Leis](tieraerzte/leis.html)
-------------------------------------------------------------
- 29.10.2025

Tierarztpraxis Paeger
-----------------------
- 30.09.2025

[Praxis Schuster](tieraerzte/finkbeiner.html)
-----------------------------------------------------------
- 01.10.2025

[Praxis Beiße](tieraerzte/beisse.html)
-----------------------------------------------------------
- 02.10.2025

[Praxis Welge](tieraerzte/welge.html)
-------------------------------------------------------------
- 03.10.2025

[Praxis Schönfeld](tieraerzte/schoenfeld.html)
-------------------------------- 
- 04.10.2025 - 05.10.2025

[Praxis Roeckemann & Orphanos](tieraerzte/roeckemann.html)
------------------------------------------------------------------------------------
- 06.10.2025

[Tierarztpraxis Lauenau - Dr. Fecht & Dr. Pohl](tieraerzte/lauenau.html)
------------------------------
- 07.10.2025

[Praxis Extertalbahn](tieraerzte/extertalbahn.html)
-----------------------------------------------------------
- 08.10.2025

Tierarztpraxis Paeger
-----------------------
- 09.10.2025

[PraxisZimmermann](tieraerzte/zimmermann.html)
---------------------------
- 10.10.2025 - 12.10.2025

[Praxis von Götz](tieraerzte/von-goetz.html)
-------------------------------------------------------------
- 13.10.2025


  
<img width="72" height="681" alt="image" src="https://github.com/user-attachments/assets/b9e88fa8-c7f5-4d79-ad74-5901ee4e2930" />




Reguläre Dienstzeiten
===================================

Wenn oben keine Praxen eingeblendet werden, dann ist heute regulärer Dienst, und Sie können sich eine Praxis mit entsprechenden Öffnungszeiten im Menüpunkt [Praxen und Kliniken](tieraerzte.html) aussuchen.



<button id="toggle_notdienst" type="button" onclick="toggle_visibility();" class="btn btn-info btn-lg btn-block" data-toggle-text="Alle Notdienst-Tage ausblenden" autocomplete="off">Alle Notdienst-Tage einblenden</button>



<!--              ACHTUNG, AB HIER NICHT MODIFIZIEREN!

Es sei denn, Sie wissen was Sie tun :-)

Der nachfolgende JavaScript-Code wird nach dem Laden dieser Seite auf dem
Computer des Nutzers ausgeführt und zeigt den jeweils gültigen Notdienst an
und versteckt die restlichen Inhalte, wenn das Datum nicht passt.
Die Zeiträume werden in Klammern in den Überschriften der ersten beiden
Stufen angegeben (also z.B. `# Überschrift (23.04.2014, 01.05.2014)`).
Mehrere Datumsangaben werden durch Komma getrennt. Es ist auch möglich
Zeiträume anzugeben, wobei ein Bindestrich das Start- vom End-Datum
abgrenzt. Beispiel `# Überschrift (23.04.2014 - 25.04.2014)`.

(C) 2014, 2019 Samuel John (www.samueljohn.de)
Released under MIT license.
-->

<script src="moment.js"></script>
<script>
// Find html nodes on the same level after `elem`, up to but excluding the
// next element in the array `stop_tags`
function siblings_up_to (elem, stop_tags) {
    var content = [];
    do {
        content.push(elem);
        elem = elem.nextElementSibling;
    } while (elem && stop_tags.indexOf(elem.tagName) < 0);
    return content;
}

function parse_date (text) {
    return moment(text, ["DD.MM.YYYY", "DD. MMM YYYY"], "de");
}

// Return a list of pairs of moment.js objects `[ ...,[start, end],...]`
function extract_dates (text) {
    // list to hold the dates
    var dates = [];
    // regular expression to extract the text in the last pair of brackets
    var find_text_in_last_brackets_regex = /^(.*)$/gm;
    var text_in_last_brackets = find_text_in_last_brackets_regex.exec(text);
    // console.log("regex matching: ", text_in_last_brackets);
    if (text_in_last_brackets && text_in_last_brackets.length > 1) {
        // if match, split out possible multiple dates seperated by `,`
        var date_ranges = text_in_last_brackets[1].split(',');
        // console.log("date_ranges: ", date_ranges);
        date_ranges.forEach(
            function (one_date_range_text) {
                var from_to = one_date_range_text.split('-');
                // console.log("from,to (array of string): ", from_to);
                if (from_to.length > 2) {
                    console.warn("Warning: More than two '-' found in date range.");
                    return;
                }
                // try to parse start...
                var start = parse_date(from_to[0]);
                var end = start.clone();
                if (start.isValid) {
                    // console.log("...start is valid: ", from_to[0]);
                    end.add('d', 1);  // set end to +24h later than start
                }
                // Check if there is a stop-date
                if (from_to.length > 1) {
                    // console.log("Stop-date given: ", from_to[1]);
                    end = parse_date(from_to[1]);
                    end.add('d', 1);  // so that 01.02.2014 - 02.02.2014 includes 02.02
                }
                // console.log("Parsed date from ", start, " to (+ 1d) ", end);
                dates.push([start, end]);
            }
        )
    }
    return dates;
}

function now_in_date_ranges ( date_ranges, duration_before, duration_after ) {
    var i = 0;
    for (; i < date_ranges.length; i++) {
        var date = date_ranges[i];
        if (date.length <= 0) {
            console.error("Could not extract dates for " + heading);
            return;
        }
        var start = date[0];
        var end = date[1];
        var now = moment();
        // console.log("start " + start._d);
        // console.log("now " + now._d);
        // console.log("end " + end._d);
        if (now >= start.subtract(duration_before) && now <= end.add(duration_after)) {
            console.log("☑ " + now.format('DD.MM.YYYY') + " is in date range: "
                        + date[0].subtract(duration_before).format('DD.MM.YYYY')
                        + " - "
                        + date[1].add(duration_after).format('DD.MM.YYYY'));
            return true; // don't hide this, let it stay visible
        } else {
            console.log("☐ " + now.format('DD.MM.YYYY'), " is NOT in date range: "
                        + date[0].subtract(duration_before).format('DD.MM.YYYY')
                        + " - "
                        + date[1].add(duration_after).format('DD.MM.YYYY'));
        }
    }
    return false;
}

// Search for h2 headings and hide them (with all the siblings) unless the
// current date (now) is in any of the given ranges (in brackest after the heading) or
// `before_now` long earlier than `now`.
function seek_and_hide () {
    // Not only show at beginning of first day but this long before already
    var duration_before = moment.duration(12, 'hours');
    var duration_after  = moment.duration(8, 'hours');
    var h2_headings = document.getElementById("content").getElementsByTagName("H2");
    console.log("seek and hide...");
    console.log("found " + h2_headings.length + " h2 headings.");
    var i = 0;
    for (; i < h2_headings.length; i++) {
        console.log("----------------- ", i );
        var heading = h2_headings[i];
        console.log("Processing " + heading.textContent);
        var follow = heading.nextElementSibling;
        var date_ranges_txt = "";
        if (follow && follow.tagName == "UL") {
            console.log("UL list after heading.");
            var lis = follow.children;
            var j = 0;
            for (; j < lis.length; j++) {
                date_ranges_txt += lis[j].textContent + ", ";
                if (! now_in_date_ranges(extract_dates(lis[j].textContent), duration_before, duration_after)) {
                    // hide
                    lis[j].display_orig = lis[j].style.display;
                    lis[j].style.display = "none";
                    lis[j].classList.add("hidden_notdienst");
                } else {
                    // show this h2
                    console.log("match found!");
                }
            }
            if( ! now_in_date_ranges(extract_dates(date_ranges_txt), duration_before, duration_after)) {
                siblings_up_to(heading, ["H2", "H1"]).forEach( function (el) {
                    el.display_orig = el.style.display;
                    el.style.display = "none";
                    el.classList.add("hidden_notdienst");
                });
                heading.classList.add("seek_and_hide");
            }
        }
        console.log("done. ", i);
    }
}

function toggle_visibility() {
    console.log("toggle_visibility");
    var hidden_elements = document.getElementsByClassName("hidden_notdienst");
    console.log(hidden_elements.length + " hidden elements...");
    var i = 0;
    for (; i < hidden_elements.length; i++) {
        console.log(hidden_elements[i] + " style = " + hidden_elements[i].style.display)
        if (hidden_elements[i].style.display == "none") {
            console.log(hidden_elements[i].display_orig);
            hidden_elements[i].style.display = hidden_elements[i].display_orig;
        } else {
            hidden_elements[i].style.display = "none";
        }
    }
}

// run this shit
seek_and_hide();
</script>









