# OCLC-simple-reclamation
Compare OCLC#s between sheets to find mismatches<br/><br/>
Record source 1: Create collection in WorldShare Collection Manager <br/>
Selection Criteria:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;li:--- [specify OCLC symbol]<br/>
Export tab delimited records: 001. Save as OCLC.xlsx in downloads folder.<br/><br/>
Record source 2: In Alma, Export bibliographic records based on logical set:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Is linked=No<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tag sync external=Publish bibliographic records<br/>
Do not specify the presence of inventory since “related records” will be cut out.<br/>
Export tab delimited records: 001, 035$a. Save as Alma.xlsx in downloads folder.
<br/><br/>
Run OCLC-simple-reclamation.py<br/><br/>
Unmatched records are the result of:<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Holding missing in OCLC, record present in Alma<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Holding present in OCLC, record missing in Alma<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. OCLC# changed in OCLC
