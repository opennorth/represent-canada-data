<?xml version="1.0" encoding="ISO-8859-1"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">
	<xsl:output method="xml" indent="yes" omit-xml-declaration="yes" doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN"
    doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd" encoding="ISO-8859-1" />
	<!--
	Document            : FGDC_FullMetaData.xsl
	Created on          : June, 2003
	BugId               : 862
	Author(program & comments) :  Christine Therriault
	Comment             :         FGDC full metadata - style full metadata in a more generic way.
	                                Can pass language (lang) and metadata translation file (for titles) 
	                                url (transFile) as params.
	                                Separated out css styling. 
	                                Included param to remove link to top for ADV preview in Discovery Portal.
	                                
	M.Adair       14-Sep-03   941   modified root element of entry          
	C.Therriault  15-Sep-03   862   modified root element of entry
	                                filtered out 'searchableData' - 'content' is a direct descendant of searchableData
	                                and as 'searchableData' element is stripped out as a candidate to be a dt beforehand,
	                                it was necessary to filter out 'content' instead.       
	                                Copied ADV_MetadataText.xml from geogratis to local.   
	C.Therriault  03-Oct-03   862   added context for ADV preview so that links to each FGDC section have rels paths.  
	C.Therriault  03-Oct-03   862   added a stringtokenizer to preserve carriage returns for description & abstract & supplemental info
	C.Therriault  14-Oct-03   1071  removed 'PRESENT' from date parsing
-->
	<xsl:param name="link">true</xsl:param>
	<xsl:key name="test-cols" match="translation" use="@name" />
	<xsl:param name="fgdcDescText" select="document('fullMetadataText.xml')/translationTable"/>
	
	<!-- Element tag names. -->
	<xsl:preserve-space elements="*"/>
	<xsl:template match="metadata">
	<html>
		<head>
		<title><xsl:value-of select="idinfo/citation/citeinfo/title"/></title>
		<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
		<style type="text/css">
			body {
				background-color: #fff;
				font-family: Arial, Helvetica, Sans-serif;
				font-size: 0.9em;
			}
						
			.metadata p {
				text-align: center;
			}
			
			.metadata dl {
				margin: 0.15em 0;
				padding: 0;
			}
			
			.metadata dt {
				margin: 0;
				padding: 0;
				color: #039;
				font-weight: bold;
			}
			
			.metadata dd {
				margin: 0 0 0 10px;
				padding: 0;
			}
			
			.metadata dl.term dt {
				float:left;
				padding-right: 0.5em;
			}
		</style>
		</head>
		<body>
		<div class="metadata">
			<h1>
				<a>
					<xsl:attribute name="name">top</xsl:attribute>
					<xsl:value-of select="idinfo/citation/citeinfo/serinfo/sername"/>
					<br/>
					<xsl:value-of select="idinfo/citation/citeinfo/title"/>
				</a>
			</h1>
			<ol>
				<xsl:for-each select="child::node()">
					<!-- links to main sections -->
					<xsl:if test="descendant::*/text()">
						<xsl:variable name="printTagValue">
							<xsl:call-template name="printTag"/>
						</xsl:variable>
						<li>
							<a>
								<xsl:attribute name="href">#<xsl:value-of select="name()"/></xsl:attribute>
								<xsl:value-of select="$printTagValue" />
							</a>
						</li>
					</xsl:if>
				</xsl:for-each>
			</ol>
			<xsl:call-template name="metadata"/>
		</div>
		</body>
	</html>
	</xsl:template>
	
	<xsl:template match="translationTable">
	  <xsl:param name="curr-label"/>
	  <xsl:value-of select="key('test-cols', $curr-label)/text[@lang=$lang]" />
 	</xsl:template>
	
	<xsl:template name="metadata">
		<xsl:for-each select="child::node()">
			<xsl:if test="string-length(text())>0 or count(child::*)>0">
				<xsl:if test="string-length(descendant::*/text())>0 or string-length(text())>0">
					<xsl:variable name="printTagValue">
						<xsl:call-template name="printTag"/>
					</xsl:variable>
					<xsl:if test="string-length(normalize-space($printTagValue))>0">
						<xsl:choose>
							<xsl:when test="name(parent::*)='metadata' and not(name()='Esri')">
								<!-- metadata children - no text -->
								<xsl:if test="not(name()='idinfo')">
									<p>
										<a>
											<xsl:attribute name="href">#top</xsl:attribute>
											<xsl:if test="$link='true'">
												<xsl:if test="$lang='fr'">Retour au haut</xsl:if>
												<xsl:if test="$lang='en'">Return to the top</xsl:if>
											</xsl:if>
										</a>
									</p>
								</xsl:if>
								<h2>
									<a>
										<xsl:attribute name="name"><xsl:value-of select="name()"/></xsl:attribute>
										<xsl:value-of select="$printTagValue"/>
									</a>
								</h2>
								<xsl:call-template name="metadata"/>
							</xsl:when>
							<xsl:otherwise>
								<xsl:choose>
									<xsl:when test="descendant::*">
										<dl>
											<dt><xsl:value-of select="$printTagValue"/>:</dt>
											<dd><xsl:call-template name="metadata"/></dd>
										</dl>
									</xsl:when>
									<xsl:otherwise>
										<dl class="term">
											<dt><xsl:value-of select="$printTagValue"/>:</dt>
											<dd><xsl:call-template name="printText"/></dd>
										</dl>
									</xsl:otherwise>
								</xsl:choose>
							</xsl:otherwise>
						</xsl:choose>
					</xsl:if>
				</xsl:if>
			</xsl:if>
		</xsl:for-each>
	</xsl:template>
	
	<xsl:template name="printTag">
		<!-- Print node name function() -->
		<xsl:variable name="title" select="name()"/>
		<xsl:apply-templates select="$fgdcDescText">
		  <xsl:with-param name="curr-label" select="$title"/>
		</xsl:apply-templates>
		
		<!--<xsl:if test="$lang='en'"><xsl:value-of select="normalize-space($fgdcDescText/translationTable/translation[@name=$title]/text[@lang=$lang])"/>:</xsl:if>
		<xsl:if test="$lang='fr'"><xsl:value-of select="normalize-space($fgdcDescText/translationTable/translation[@name=$title]/text[@lang=$lang])"/> :</xsl:if>
		-->
	</xsl:template>
	<xsl:template name="printText">
		<!-- Print text function() -->
		<!--span-->
			<xsl:choose>
				<!--Link formatting-->
				<xsl:when test="starts-with(text(),'http')">
					<a>
						<xsl:attribute name="href"><xsl:value-of select="text()"/></xsl:attribute>
						<xsl:value-of select="text()"/>
					</a>
				</xsl:when>
				<!--Mailto formatting-->
				<xsl:when test="name()='cntemail'">
					<a>
						<xsl:attribute name="href">mailto:<xsl:value-of select="text()"/></xsl:attribute>
						<xsl:value-of select="text()"/>
					</a>
				</xsl:when>
				<!--Date formatting-->
				<xsl:when test="(name()='pubdate' or name()='caldate' or name()='begdate' or name()='enddate' or name()='metd' or name()='metrd' or name()='metfrd' or name()='procdate') and not(string(number(text()))='NaN')">
					<xsl:choose>
						<xsl:when test="string-length(text())=8">
							<xsl:value-of select="substring(text(),1,4)"/>-<xsl:value-of select="substring(text(),5,2)"/>-<xsl:value-of select="substring(text(),7,2)"/>
						</xsl:when>
						<xsl:when test="string-length(text())=6">
							<xsl:value-of select="substring(text(),1,4)"/>-<xsl:value-of select="substring(text(),5,2)"/>
						</xsl:when>
						<xsl:otherwise>
							<xsl:value-of select="text()"/>
						</xsl:otherwise>
					</xsl:choose>
				</xsl:when>
				<xsl:when test="name()='purpose' or name()='abstract' or name()='supplinf' or name()='procdesc' or name()='logic' or name()='srccontr' or name()='complete' or name()='atttraccr' or name()='horizpar' or name()='vertaccr' or name()='horizpae' or name()='vertccr' or name()='metuc'">
					<xsl:call-template name="tokenize">
						<xsl:with-param name="str" select="text()"/>
						<xsl:with-param name="sep" select="'&#xA;'"/>
					</xsl:call-template>
				</xsl:when>
				<xsl:otherwise>
					<xsl:value-of select="text()"/>
				</xsl:otherwise>
			</xsl:choose>
		<!--/span-->
	</xsl:template>
	<xsl:template name="tokenize">
		<!-- tokenize a string -->
		<xsl:param name="str"/>
		<!-- String to process -->
		<xsl:param name="sep"/>
		<!-- Legal separator character -->
		<xsl:choose>
			<xsl:when test="contains($str,$sep)">
				<!-- Only tokenize if there is a separator present in the string -->
				<xsl:call-template name="process-token">
					<!-- Process the token before the separator -->
					<xsl:with-param name="token" select="substring-before($str,$sep)"/>
				</xsl:call-template>
				<xsl:call-template name="tokenize">
					<!-- Re-tokenize the new string which is contained after the separator -->
					<xsl:with-param name="str" select="substring-after($str,$sep)"/>
					<xsl:with-param name="sep" select="'&#xA;'"/>
					<!-- carriage return -->
				</xsl:call-template>
			</xsl:when>
			<xsl:otherwise>
				<!-- If there is nothing else to tokenize, just treat the last part of the str as a regular token -->
				<xsl:call-template name="process-token">
					<xsl:with-param name="token" select="$str"/>
				</xsl:call-template>
			</xsl:otherwise>
		</xsl:choose>
	</xsl:template>
	<xsl:template name="process-token">
		<!-- process - separate with <br> -->
		<xsl:param name="token"/>
		<!-- token to process -->
		<xsl:value-of select="$token"/>
		<br/>
	</xsl:template>
</xsl:stylesheet>
