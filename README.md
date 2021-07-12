# OCLC-simple-reclamation
Compare OCLC#s between sheets to find mismatches<br/><br/>
Record source 1: Create collection in WorldShare Collection Manager <br/>
Selection Criteria:<br/>
li:---<br/>
Export tab delimited records: 001. Save as Alma.xlsx in downloads folder.<br/><br/>
Record source 2: In Alma, export Bibliographic Records based on logical set:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is linked=No<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tag sync external=Publish bibliographic records<br/>
Do not specify the presence of inventory since “related records” will be cut out.<br/>
Export tab delimited records: 001, 035$a. Save as OCLC.xlsx in downloads folder.<br/>
<br/><br/>
Run OCLC-simple-reclamation.py
