%!PS-Adobe-3.0
%APL_DSC_Encoding: UTF8
%APLProducer: (Version 10.14.3 (Build 18D109) Quartz PS Context)
%%Title: (Untitled)
%%Creator: (Aquamacs: cgpdftops CUPS filter)
%%CreationDate: (Monday, March 25 2019 21:19:09 CET)
%%For: (Steeve SAAH)
%%DocumentData: Clean7Bit
%%LanguageLevel: 2
%%PageOrder: Ascend
%RBINumCopies: 1
%%Pages: (atend)
%%BoundingBox: (atend)
%%EndComments
userdict/dscInfo 5 dict dup begin
/Title(Untitled)def
/Creator(Aquamacs: cgpdftops CUPS filter)def
/CreationDate(Monday, March 25 2019 21:19:09 CET)def
/For(Steeve SAAH)def
/Pages 1 def
end put
%%BeginProlog
%%BeginFile: lw8_errorhandler-2.0
/currentpacking where 
	{ pop /oldpack currentpacking def /setpacking where
		{
			pop false setpacking
		}if
	}if
/$brkpage 64 dict def $brkpage begin
/prnt
 {dup type/stringtype ne{=string cvs}if dup length 6 mul/tx exch def/ty 10 def
  currentpoint/toy exch def/tox exch def 1 setgray newpath
  tox toy 2 sub moveto 0 ty rlineto tx 0 rlineto 0 ty neg rlineto
  closepath fill tox toy moveto 0 setgray show}bind def
/nl{currentpoint exch pop lmargin exch moveto 0 -10 rmoveto}def
/=={/cp 0 def typeprint nl}def
/typeprint{dup type exec}readonly def
/lmargin 72 def
/rmargin 72 def
/tprint
   {dup length cp add rmargin gt{nl/cp 0 def}if
    dup length cp add/cp exch def prnt}readonly def
/cvsprint{=string cvs tprint( )tprint}readonly def
/integertype{cvsprint}readonly def
/realtype{cvsprint}readonly def
/booleantype{cvsprint}readonly def
/operatortype{(--)tprint =string cvs tprint(-- )tprint}readonly def
/marktype{pop(-mark- )tprint}readonly def
/dicttype{pop(-dictionary- )tprint}readonly def
/nulltype{pop(-null- )tprint}readonly def
/filetype{pop(-filestream- )tprint}readonly def
/savetype{pop(-savelevel- )tprint}readonly def
/fonttype{pop(-fontid- )tprint}readonly def
/nametype{dup xcheck not{(/)tprint}if cvsprint}readonly def
/stringtype
 {dup rcheck{(\()tprint tprint(\))tprint}{pop(-string- )tprint}ifelse
 }readonly def
/arraytype
 {dup rcheck{dup xcheck
  {({)tprint{typeprint}forall(})tprint}
  {([)tprint{typeprint}forall(])tprint}ifelse}{pop(-array- )tprint}ifelse
 }readonly def
/packedarraytype
 {dup rcheck{dup xcheck
  {({)tprint{typeprint}forall(})tprint}
  {([)tprint{typeprint}forall(])tprint}ifelse}{pop(-packedarray- )tprint}ifelse
 }readonly def
/courier/Courier findfont 10 scalefont def
end %$brkpage
errordict/handleerror
 {systemdict begin $error begin $brkpage begin newerror
   {/newerror false store 
    vmstatus pop pop 0 ne{grestoreall}if initgraphics courier setfont
    lmargin 720 moveto(ERROR: )prnt errorname prnt
    nl(OFFENDING COMMAND: )prnt/command load prnt
 	$error/ostack known{
	$error/ostack get type dup/arraytype eq exch /packedarraytype eq or
   {nl nl(STACK:)prnt nl nl $error/ostack get aload length{==}repeat}if}if
    systemdict/showpage get exec(%%[ Error: )print
    errorname =print(; OffendingCommand: )print/command 
    load =print( ]%%)= flush}if end end end}
dup 0 systemdict put dup 4 $brkpage put bind readonly put
/currentpacking where 
	{ pop  /setpacking where
		{
			pop oldpack setpacking
		}if
	}if
%%EndFile
%%BeginFile: cg-pdf.ps
%%Copyright: Copyright 2000-2004 Apple Computer Incorporated.
%%Copyright: All Rights Reserved.
currentpacking true setpacking
/cg_md 141 dict def
cg_md begin
/L3? languagelevel 3 ge def
/bd{bind def}bind def
/ld{load def}bd
/xs{exch store}bd
/xd{exch def}bd
/cmmtx matrix def
mark
/sc/setcolor
/scs/setcolorspace
/dr/defineresource
/fr/findresource
/T/true
/F/false
/d/setdash
/w/setlinewidth
/J/setlinecap
/j/setlinejoin
/M/setmiterlimit
/i/setflat
/rc/rectclip
/rf/rectfill
/rs/rectstroke
/f/fill
/f*/eofill
/sf/selectfont
/s/show
%/as/ashow
/xS/xshow
/yS/yshow
/xyS/xyshow
/S/stroke
/m/moveto
/l/lineto
/c/curveto
/h/closepath
/n/newpath
/q/gsave
/Q/grestore
counttomark 2 idiv
%dup (number of ld's = )print == flush	% *** how many 
{ld}repeat pop
/SC{	% CSname
    /ColorSpace fr scs
}bd
/sopr /setoverprint where{pop/setoverprint}{/pop}ifelse ld
/soprm /setoverprintmode where{pop/setoverprintmode}{/pop}ifelse ld
/cgmtx matrix def
/sdmtx{cgmtx currentmatrix pop}bd
/CM {cgmtx setmatrix}bd		% pop the ctm: our gstate ctm on host is now identity
/cm {cmmtx astore CM concat}bd	% reset the matrix and then concat
/W{clip newpath}bd
/W*{eoclip newpath}bd

statusdict begin product end dup (HP) anchorsearch{
    pop pop pop	% pop off the search results
    true
}{
    pop	% previous search result
   (hp) anchorsearch{
	pop pop true
    }{
	pop false
    }ifelse
}ifelse

{	% HP is the product: we use this method of stroking because of a bug in their clone printers with certain T3 fonts
    { 
	{ % charCode Wx Wy
	    pop pop % charCode
	    (0)dup 0 4 -1 roll put
	    F charpath
	}cshow
    }
}{
    {F charpath}
}ifelse
/cply exch bd
/cps {cply stroke}bd
/pgsave 0 def
/bp{/pgsave save store}bd
/ep{pgsave restore showpage}def		% dont' bind
/re{4 2 roll m 1 index 0 rlineto 0 exch rlineto neg 0 rlineto h}bd

/scrdict 10 dict def
/scrmtx matrix def
/patarray 0 def
/createpat{patarray 3 1 roll put}bd
/makepat{
scrmtx astore pop
gsave
initgraphics
CM 
patarray exch get
scrmtx
makepattern
grestore
setpattern
}bd

/cg_BeginEPSF{
    userdict save/cg_b4_Inc_state exch put
    userdict/cg_endepsf/cg_EndEPSF load put
    count userdict/cg_op_count 3 -1 roll put 
    countdictstack dup array dictstack userdict/cg_dict_array 3 -1 roll put
    3 sub{end}repeat
    /showpage {} def
    0 setgray 0 setlinecap 1 setlinewidth 0 setlinejoin
    10 setmiterlimit [] 0 setdash newpath
    false setstrokeadjust false setoverprint	% don't use F
}bd
/cg_EndEPSF{
  countdictstack 3 sub { end } repeat
  cg_dict_array 3 1 index length 3 sub getinterval
  {begin}forall
  count userdict/cg_op_count get sub{pop}repeat
  userdict/cg_b4_Inc_state get restore
  F setpacking
}bd

/cg_biproc{currentfile/RunLengthDecode filter}bd
/cg_aiproc{currentfile/ASCII85Decode filter/RunLengthDecode filter}bd
/ImageDataSource 0 def
L3?{
    /cg_mibiproc{pop pop/ImageDataSource{cg_biproc}def}bd
    /cg_miaiproc{pop pop/ImageDataSource{cg_aiproc}def}bd
}{
    /ImageBandMask 0 def
    /ImageBandData 0 def
    /cg_mibiproc{
	string/ImageBandMask xs
	string/ImageBandData xs
	/ImageDataSource{[currentfile/RunLengthDecode filter dup ImageBandMask/readstring cvx
	    /pop cvx dup ImageBandData/readstring cvx/pop cvx]cvx bind}bd
    }bd
    /cg_miaiproc{	
	string/ImageBandMask xs
	string/ImageBandData xs
	/ImageDataSource{[currentfile/ASCII85Decode filter/RunLengthDecode filter
	    dup ImageBandMask/readstring cvx
	    /pop cvx dup ImageBandData/readstring cvx/pop cvx]cvx bind}bd
    }bd
}ifelse
/imsave 0 def
/BI{save/imsave xd mark}bd
/EI{imsave restore}bd
/ID{
counttomark 2 idiv
dup 2 add	% leave room for imagetype and imagematrix
dict begin
{def} repeat
pop		% remove mark
/ImageType 1 def
/ImageMatrix[Width 0 0 Height neg 0 Height]def
currentdict dup/ImageMask known{ImageMask}{F}ifelse exch
% currentdict on stack
L3?{
    dup/MaskedImage known
    { 
	pop
	<<
	    /ImageType 3
	    /InterleaveType 2
	    /DataDict currentdict
	    /MaskDict
	    <<  /ImageType 1
		/Width Width
		/Height Height
		/ImageMatrix ImageMatrix
		/BitsPerComponent 1
		/Decode [0 1]
		currentdict/Interpolate known
		{/Interpolate Interpolate}if
	    >>
	>>
    }if
}if
exch
{imagemask}{image}ifelse	
end	% pop imagedict from dict stack
}bd

/cguidfix{statusdict begin mark version end
{cvr}stopped{cleartomark 0}{exch pop}ifelse
2012 lt{dup findfont dup length dict begin
{1 index/FID ne 2 index/UniqueID ne and
{def} {pop pop} ifelse}forall
currentdict end definefont pop
}{pop}ifelse
}bd
/t_array 0 def
/t_i 0 def
/t_c 1 string def
/x_proc{ % x y
    exch t_array t_i get add exch moveto
    /t_i t_i 1 add store
}bd
/y_proc{ % x y
    t_array t_i get add moveto
    /t_i t_i 1 add store
}bd
/xy_proc{
        % x y
	t_array t_i 2 copy 1 add get 3 1 roll get 
	4 -1 roll add 3 1 roll add moveto
	/t_i t_i 2 add store
}bd
/sop 0 def		% don't bind sop
/cp_proc/x_proc ld 	% default moveto proc is for xwidths only
/base_charpath		% string array
{
    /t_array xs
    /t_i 0 def
    { % char
	t_c 0 3 -1 roll put
        currentpoint
	t_c cply sop
        cp_proc
    }forall
    /t_array 0 def
}bd
/sop/stroke ld		% default sop is stroke. Done here so we don't bind in /base_charpath 

% default sop is stroke
/nop{}def
/xsp/base_charpath ld
/ysp{/cp_proc/y_proc ld base_charpath/cp_proc/x_proc ld}bd
/xysp{/cp_proc/xy_proc ld base_charpath/cp_proc/x_proc ld}bd
/xmp{/sop/nop ld /cp_proc/x_proc ld base_charpath/sop/stroke ld}bd
/ymp{/sop/nop ld /cp_proc/y_proc ld base_charpath/sop/stroke ld}bd
/xymp{/sop/nop ld /cp_proc/xy_proc ld base_charpath/sop/stroke ld}bd
/refnt{ % newname encoding fontname
findfont dup length dict copy dup
/Encoding 4 -1 roll put 
definefont pop
}bd
/renmfont{ % newname fontname
findfont dup length dict copy definefont pop
}bd

L3? dup dup{save exch}if

% languagelevel2 ONLY code goes here

/Range 0 def
/DataSource 0 def
/val 0 def
/nRange 0 def
/mulRange 0 def
/d0 0 def
/r0 0 def
/di 0 def
/ri 0 def
/a0 0 def
/a1 0 def
/r1 0 def
/r2 0 def
/dx 0 def
/Nsteps 0 def
/sh3tp 0 def
/ymax 0 def
/ymin 0 def
/xmax 0 def
/xmin 0 def

/setupFunEval % funDict -- 	% this calculates and sets up a function dict for evaulation.
{
    begin
	/nRange Range length 2 idiv store
	/mulRange   % precompute the range data needed to map a sample value from the table to a range value
		    % this data looks like [ range0mul range0min range1mul range1min ... rangeN-1mul rangeN-1min ]
	[ 
	    0 1 nRange 1 sub
	    { % index
		    2 mul/nDim2 xd		% 2*dimension# we are dealing with
		    Range nDim2 get		% ymin
		    Range nDim2 1 add get	% ymin ymax 
		    1 index sub			% ymin (ymax-ymin)
						% xmin = 0, xmax = 255 (2^bitspersample - 1)
		    255 div			% ymin (ymax-ymin)/(xmax - xmin)
		    exch			% (ymax-ymin)/(xmax - xmin) ymin
	    }for
	]store
    end
}bd

/FunEval % val1 fundict -> comp1 comp2 ... compN
{
    begin
	% the value passed in is the base index into the table
	nRange mul /val xd	% compute the actual index to the table
				% since there are nRange entries per base index
	0 1 nRange 1 sub
	{
	    dup 2 mul/nDim2 xd % dim
	    val	% base value to use to do our lookup
	    add DataSource exch get %  lookedupval
	    mulRange nDim2 get mul 	% lookedupval*(ymax-ymin)/(xmax-xmin)
	    mulRange nDim2 1 add get % lookedupval*(ymax-ymin)/(xmax-xmin) ymin
	    add % interpolated result
	}for	% comp1 comp2 ... compN
    end
}bd

/max % a b -> max(a, b)
{
	2 copy lt
	{exch pop}{pop}ifelse
}bd

/sh2
{	% emulation of shading type 2. Assumes shading dictionary is top dictionary on the dict stack
	/Coords load aload pop 	% x0 y0 x1 y1
	3 index 3 index translate	% origin is now at beginning point of shading
					% x0 y0 x1 y1
	3 -1 roll sub	% x0 x1 y1-y0
	3 1 roll exch 	% y1-y0 x1 x0
	sub				% y1-y0 x1-x0
	2 copy
	dup mul exch dup mul add sqrt	% length of segment between two points
	dup
	scale  
	atan	% atan (dy/dx)
	%dup (rotation angle = )print ==
	rotate		% now line between 0,0 and 1,0 is the line perpendicular to which the axial lines are drawn					
	
	/Function load setupFunEval	% may need to setup function dictionary by calling setupFunEval
	
	% this is now specific to axial shadings. Compute the maximum bounds to fill
	clippath {pathbbox}stopped {0 0 0 0}if newpath 	% x0 y0 x1 y1
	/ymax xs
	/xmax xs
	/ymin xs
	/xmin xs
	currentdict/Extend known
	{
		/Extend load 0 get
		{	
			0/Function load FunEval sc	% evaluate the function to get a color and set it
			xmin ymin xmin abs ymax ymin sub rectfill
		}if
	}if
	% paint the rects. The sampling frequency is that of our table
	/Nsteps/Function load/Size get 0 get 1 sub store
	/dx 1 Nsteps div store
	gsave
		/di ymax ymin sub store
		/Function load
		% loop Nsteps + 1 times, incrementing the index by 1 each time
		0 1 Nsteps
		{
			1 index FunEval sc
			0 ymin dx di rectfill
			dx 0 translate
		}for
		pop	% pop our function
	grestore	% origin is back to start point
	currentdict/Extend known
	{
		/Extend load 1 get
		{	
			Nsteps/Function load FunEval sc	% last element
			1 ymin xmax 1 sub abs ymax ymin sub rectfill
		}if
	}if
}bd

/shp	% this paints our shape for shading type 3
{	% x1 r1 x0 r0 -
	4 copy

	% fill interior arc
	dup 0 gt{
		0 exch a1 a0 arc
	}{
		pop 0 moveto
	}ifelse

	dup 0 gt{
		0 exch a0 a1 arcn
	}{
		pop 0 lineto
	}ifelse
	
	fill

	% fill exterior arc
	dup 0 gt{
		0 exch a0 a1 arc
	}{
		pop 0 moveto
	}ifelse

	dup 0 gt{
		0 exch a1 a0 arcn
	}{
		pop 0 lineto
	}ifelse
	
	fill
}bd

/calcmaxs
{	% calculate maximum distance vector from origin to corner points
	% of bbox
	xmin dup mul ymin dup mul add sqrt		% (xmin2 + ymin2)
	xmax dup mul ymin dup mul add sqrt		% (xmax2 + ymin2)
	xmin dup mul ymax dup mul add sqrt		% (xmin2 + ymax2)
	xmax dup mul ymax dup mul add sqrt		% (xmax2 + ymax2)
	max max max								% maximum value
}bd

/sh3
{	% emulation of shading type 3. Assumes shading dictionary is top dictionary on the dict stack
	/Coords load aload pop 	% x0 y0 r1 x1 y1 r2
	5 index 5 index translate	% origin is now at first circle origin
	3 -1 roll 6 -1 roll sub		% y0 r1 y1 r2 dx
	3 -1 roll 5 -1 roll sub		% r1 r2 dx dy
	2 copy dup mul exch dup mul add sqrt
	/dx xs						% r1 r2 dx dy
	2 copy 0 ne exch 0 ne or
	{
		% r1 r2 dx dy
		exch atan rotate	% we are now rotated so dy is zero and positive values of dx move us as expected
	}{
		pop pop
	}ifelse
	% r1 r2		
	/r2 xs
	/r1 xs
	/Function load 
	dup/Size get 0 get 1 sub	% this is the size of our table minus 1
	/Nsteps xs		% at some point we should optimize this better so NSteps is based on needed steps for the device
	setupFunEval		% may need to setup function dictionary by calling setupFunEval
	% determine the case:
	% case 0: circle1 inside circle2
	% case 1: circle 2 inside circle 1
	% case 2: r1 = r2 
	% case 3: r1 != r2
	dx r2 add r1 lt{
		% circle 2 inside of circle 1
		0 
	}{
		dx r1 add r2 le
		{ % circle 1 inside of circle 2
			1
		}{ % circles don't contain each other
			r1 r2 eq
			{	% equal
				2
			}{ % r1 != r2
				3
			}ifelse		
		}ifelse
	}ifelse
	/sh3tp xs		% sh3tp has the number of our different cases
	clippath {pathbbox}stopped {0 0 0 0}if 
	newpath 	% x0 y0 x1 y1
	/ymax xs
	/xmax xs
	/ymin xs
	/xmin xs

	% Arc angle atan( sqrt((dx*dx + dy*dy) - dr*dr), dr)
	dx dup mul r2 r1 sub dup mul sub dup 0 gt
	{
		sqrt r2 r1 sub atan
		/a0 exch 180 exch sub store 
		/a1 a0 neg store 
	}{
		pop
		/a0 0 store
		/a1 360 store		
	}ifelse		

	currentdict/Extend known
	{
		/Extend load 0 get r1 0 gt and	% no need to extend if the radius of the first end is 0
		{	
			0/Function load FunEval sc	% evaluate the function to get a color and set it
			% case 0: circle1 inside circle2
			% case 1: circle 2 inside circle 1
			% case 2: circles don't contain each other and r1 == r2
			% case 3: circles don't contain each other and r1 != r2
			{ 
				{	% case 0
					dx 0 r1 360 0 arcn
					xmin ymin moveto
					xmax ymin lineto
					xmax ymax lineto
					xmin ymax lineto
					xmin ymin lineto
					eofill		% for the bigger radius we fill everything except our circle
				}
				{	% case 1
					r1 0 gt{0 0 r1 0 360 arc fill}if
				}
				{	% case 2
					% r1 == r2, extend 0
					% r3 = r, x3 = -(abs(minx) + r), x1 = 0
				
					% x(i+1) r(i+1) x(i) r(i) shp
					0 r1 xmin abs r1 add neg r1 shp
				}
				{	% case 3
					% no containment, r1 != r2
				
					r2 r1 gt{	% the endpoint we are drawing is that with a circle of zero radius
						% x(i+1) r(i+1) x(i) r(i) shp
						0 r1
						r1 neg r2 r1 sub div dx mul	% this is point of beginning circle
						0	% point of ending circle
						shp	% takes x(i+1) r(i+1) x(i) r(i)
					}{	% the first circle is the bigger of the two
						% we find a circle on our line which is outside the bbox in the
						% negative direction
						% x(i+1) r(i+1) x(i) r(i) shp
						0 r1 calcmaxs	% 0 r1 maxs
						dup
						% calculating xs: (-(maxs+r2)*x2)/(x2-(r1-r2))
						r2 add dx mul dx r1 r2 sub sub div
						neg				% maxs xs'
						exch 1 index	% xs' maxs xs'
						abs exch sub
						shp
					}ifelse
				} 
			}sh3tp get exec	% execute the extend at beginning proc for our shading type
		}if
	}if

	% now do the shading
	/d0 0 store
	/r0 r1 store
	/di dx Nsteps div store
	/ri r2 r1 sub Nsteps div store 
	/Function load 
	0 1 Nsteps
	{	% function t(i)
		1 index FunEval sc
		d0 di add r0 ri add d0 r0 shp
		{
		% fill interior arc
		d0 0 r0 a1 a0 arc
		d0 di add 0 r0 ri add a0 a1 arcn
		fill
		
		% fill exterior arc
		d0 0 r0 a0 a1 arc
		d0 di add 0 r0 ri add a1 a0 arcn
		fill
		}pop
		
		% advance to next
		/d0 d0 di add store
		/r0 r0 ri add store
	}for
	pop	% pop our function dict

	% handle Extend
	currentdict/Extend known
	{
		/Extend load 1 get r2 0 gt and	% no need to extend if the radius of the last end is 0
		{	
			Nsteps/Function load FunEval sc	% last element
			% case 0: circle1 inside circle2
			% case 1: circle 2 inside circle 1
			% case 2: circles don't contain each other and r1 == r2
			% case 3: circles don't contain each other and r1 != r2
			{ 
				{
					dx 0 r2 0 360 arc fill
				} 
				{
					dx 0 r2 360 0 arcn
					xmin ymin moveto
					xmax ymin lineto
					xmax ymax lineto
					xmin ymax lineto
					xmin ymin lineto
					eofill		% for the bigger radius we fill everything except our circle
				} 
				{	% r1 == r2, extend 1
					% r3 = r, x3 = (abs(xmax) + r), x1 = dx
					% x(i+1) r(i+1) x(i) r(i) shp
					xmax abs r1 add r1 dx r1 shp
				}	
				{	% no containment, r1 != r2
			
					r2 r1 gt{
						% we find a circle on our line which is outside the bbox in the
						% positive direction
						% x(i+1) r(i+1) x(i) r(i) shp
						calcmaxs dup	% maxs maxs
						% calculating xs: ((maxs+r1)*x2)/(x2-(r2-r1))
						r1 add dx mul dx r2 r1 sub sub div	% maxs xs
						exch 1 index	% xs maxs xs
						exch sub
						dx r2
						shp
					}{	% the endpoint we are drawing is that with a circle of zero radius
						% x(i+1) r(i+1) x(i) r(i) shp
						r1 neg r2 r1 sub div dx mul	% this is point of ending circle
						0		% radius of ending circle
						dx 		% point of starting circle
						r2		% radius of starting circle
						shp
					}ifelse
				}
			}			
			sh3tp get exec	% execute the extend at end proc for our shading type
		}if
	}if
}bd
/sh		% emulation of shfill operator for type 2 and type 3 shadings based on type 0 functions
{	% shadingDict --
	begin
		/ShadingType load dup dup 2 eq exch 3 eq or
		{	% shadingtype
			gsave
				newpath
				/ColorSpace load scs
				currentdict/BBox known
				{
					/BBox load aload pop	% llx lly urx ury
					2 index sub				% llx lly urx ury-lly
					3 index					% llx lly urx ury-lly llx
					3 -1 roll exch sub 
					exch rectclip
				}if
				2 eq
				{sh2}{sh3}ifelse
			grestore
		}{
			% shadingtype
			pop 
			(DEBUG: shading type unimplemented\n)print flush
		}ifelse
	end
}bd

% end of language level 2 ONLY code

{restore}if not dup{save exch}if
% languagelevel3 ONLY code goes here
	L3?{	% we do these loads conditionally or else they will fail on a level 2 printer
		/sh/shfill ld
		/csq/clipsave ld
		/csQ/cliprestore ld
	}if
{restore}if

%currentdict dup maxlength exch length sub (number of extra slots in md = )print == flush	% *** how many entries are free
end
setpacking
% count 0 ne { pstack(***extras on stack during prolog execution***\n)print flush}if	% *** BARK if anything is left on stack
%%EndFile
%%EndProlog
%%BeginSetup
% Disable CTRL-D as an end-of-file marker...
userdict dup(\004)cvn{}put (\004\004)cvn{}put
[{
%%BeginFeature: *PageSize A4
<</PageSize[595.00 842.00]>>setpagedevice
%%EndFeature
} stopped cleartomark
% x y w h ESPrc - Clip to a rectangle.
userdict/ESPrc/rectclip where{pop/rectclip load}
{{newpath 4 2 roll moveto 1 index 0 rlineto 0 exch rlineto
neg 0 rlineto closepath clip newpath}bind}ifelse put
% x y w h ESPrf - Fill a rectangle.
userdict/ESPrf/rectfill where{pop/rectfill load}
{{gsave newpath 4 2 roll moveto 1 index 0 rlineto 0 exch rlineto
neg 0 rlineto closepath fill grestore}bind}ifelse put
% x y w h ESPrs - Stroke a rectangle.
userdict/ESPrs/rectstroke where{pop/rectstroke load}
{{gsave newpath 4 2 roll moveto 1 index 0 rlineto 0 exch rlineto
neg 0 rlineto closepath stroke grestore}bind}ifelse put
userdict/ESPwl{}bind put
%%EndSetup
%%Page: 1 1
%%PageBoundingBox: 0 0 595 842
%%BeginPageSetup
%%EndPageSetup
cg_md begin
bp
sdmtx
%RBIBeginFontSubset: PQWPDK+Monaco
%!FontType1-1.0: PQWPDK+Monaco 1.0000.2.0000
14 dict begin/FontName /PQWPDK+Monaco def
/PaintType 0 def
/Encoding 256 array 0 1 255{1 index exch/.notdef put}for
dup 33 /a put
dup 34 /equal put
dup 35 /five put
dup 36 /p put
dup 37 /r put
dup 38 /i put
dup 39 /n put
dup 40 /t put
dup 41 /parenleft put
dup 42 /parenright put
dup 43 /y put
dup 44 /h put
dup 45 /o put
readonly def
42/FontType resourcestatus{pop pop false}{true}ifelse
%APLsfntBegin
{currentfile 0(%APLsfntEnd\n)/SubFileDecode filter flushfile}if
/FontType 42 def
/FontMatrix matrix def
/FontBBox[2048 -1249 1 index div -862 2 index div 1647 3 index div 2504 5 -1 roll div]cvx def
/sfnts [<
74727565000900000000000063767420000000000000009C000003F66670676D000000000000049400000518676C796600000000000009AC00000B186865616400000000000014C4000000366868656100000000000014FC00000024686D74780000000000001520000000386C6F636100000000000015580000001E6D6178700000000000001578000000207072657000000000000015980000053E064E001F0610002F0610002E045D001F0000FFD10000FFE10000FFD1FE4EFFE1066D0000FE8C0000026D001700BE000000BE0000000000000000009B00BA00BA0047007C007C009B00CA009B009B009B00BA00B3016A01C2FFB800CA009B043E009100F801B300CA00020076FFFF004800B4009B00AB0021002E007E0114000F00C2011F009B009C021F00100021007E009B014901B1FE44000B00380057020DFF71003E00C900C903CE0021005D007D008D0095009D00AC011101400146019001C6FF4C00BA00BC017101D104CAFFA90002001F002F00470099009B00BA00C20146014F01710008001F002E004A005D009701B80374048CFF63FF82FF8AFFD00014001F004F005D006A007C007E009B009B00B400D300D9020A02CA03A303CAFEB5FEE3FF53FF73FF7EFFB8FFE0FFE0FFE000480074007D008D0094009900A300B600BA00BA00C900E200F8019801F1036503AB04460452FF2DFF67FF82FFFF00010020002D003E00470055005600720075007A009900BA00DB00E300F800FA011F0127012E01430155017A019001D7021F0241024D0327034603B203CA041F042F0465047B066DFDE0FE73FF0EFFB000050033004800540065006F007D007E007F0091009B00AB00BA00F8010001110117012A0155015801A301A901E902000217022C02300249024E0265026D02F90314035403550361048C07B2FE29FE9DFEF8FF07FF47FF99FFA1000100020004000800080019001E0027002900300036003F0048004F00550056005F00630066006C00740076008500940098009900BC00BC00C100C100CB00CB00CD00D000DB00F000F200F800F900FA01080111011F0127012E01360143015701630175018001B201BB01C701D101D501E301E901F8024B029802AB02BC02F00308036C0374038C03AB03CA03D903E103E103F803FC041F041F042704560551FC05FE98FEC8FEEFFFC1FFD0002800300067006D0084009300A900B400BA00C500C600D100D200E200EA00F000F000F50103010F011001110118011F0133013401380138013F014A015601590168016D0175017C01810194019B01B201B201CA01D101F102050218024A028C029402AA02DA02E103080327033F03460346038C03A303FB041F043E043E043F0465046D0484048A04A404CA057405EC0610078407E100BE00CA00BD00C200000000000000000000000000AB00A3
07C20084009D009B00B200D000AB009A007A00BB00AB00BA006C00AB04C600ED011F011F0172011C0146023600DB0120006E021A018B01C4014E022202A301A901E901780308021F0000000000CA00B801CD025D059C00FA026D014F0202014F01D1021E00AB0485007C00A3FBE7FC9B0324FCDBFE840382FC50FD9B050800200079008B00DD0392041F00AC00820030002A0000403231302F2E2D2C2B2A292827262524232221201F1E1D1C1B1A191817161514131211100F0E0D0C0B0A090807060504030201002C4523466020B02660B004262348482D2C452346236120B02661B004262348482D2C45234660B0206120B04660B004262348482D2C4523462361B0206020B02661B02061B004262348482D2C45234660B0406120B06660B004262348482D2C4523462361B0406020B02661B04061B004262348482D2C0110203C003C2D2C20452320B0CD442320B8015A51582320B08D44235920B0ED51582320B04D44235920B0042651582320B00D44235921212D2C20204518684420B001602045B04676688A4560442D2C01B9400000000A2D2C00B9000040000B2D2C2045B00043617D6818B0004360442D2C45B01A234445B01923442D2C2045B00325456164B050515845441B2121592D2CB00143632362B0002342B00F2B2D2C2045B0004360442D2C01B00743B006430A2D2C2069B04061B0008B20B12CC08A8CB8100062602B0C642364615C58B00361592D2C45B0112BB0172344B0177AE4182D2CB801A65458B00943B801005458B9001AFF80B11980444459592D2C45B0112BB017458CB0172344B0177AE5182D2CB002254661658A46B040608B482D2CB0022546608A46B040618C482D2C01182F2D2C20B0032545B019234445B01A23444565234520B00325606A20B009234223688A6A606120B01A8AB000527921B21A1A40B9FFE0001A45208A54582321B03F1B235961441CB114008A5279B31940201945208A54582321B03F1B235961442D2CB9187E3B210B2D2CB92D412D410B2D2CB93B21187E0B2D2CB93B21E7830B2D2CB92D41D2C00B2D2CB9187EC4E00B2D2C4B525845441B2121592D2C0120B003252349B04060B0206320B000525823B002253823B002256538008A63381B212121212159012D2C4569B00943608A103A2D2C01B005251023208AF500B0016023EDEC2D2C01B005251023208AF500B0016123EDEC2D2C01B0062510F500EDEC2D2C20B001600110203C003C2D2C20B001610110203C003C2D2CB02B2BB02A2A2D2C00B0064365B007430B2D2C3EB02A2A2D2C352D2C76B01B23701020B01B4520B0005058B00161593A2F182D2C21210C6423648BB84000622D2C21B08051580C6423648BB82000621BB200402F2B59B002602D2C21B0C051580C6423648BB81555621BB200802F2B59B002602D2C0C64
23648BB84000626023212D2CB4000100000015B00826B00826B00826B008260F10161345683AB001162D2CB4000100000015B00826B00826B00826B008260F1016134568653AB001162DB800322C4BB800095058B101018E59B801FF85B800441DB9000900035F5E2DB800332C2020456944B001602DB800342CB800332A212DB800352C2046B003254652582359208A208A49648A204620686164B004254620686164525823658A592F20B00053586920B000545821B040591B6920B000545821B0406559593A2DB800362C2046B00425465258238A592046206A6164B0042546206A61645258238A592FFD2DB800372C4B20B0032650585158B080441BB04044591B21212045B0C05058B0C0441B2159592DB800382C2020456944B001602020457D691844B001602DB800392CB800382A2DB8003A2C4B20B003265358B0801BB040598A8A20B0032653582321B0C08A8A1B8A235920B0032653582321B801008A8A1B8A235920B0032653582321B801408A8A1B8A235920B80003265358B0032545B8018050582321B8018023211BB003254523212321591B2159442DB8003B2C4B535845441B2121592D000200930000036D0610000300070045400907061D0104051D0302B801A340120000010A04071D03001A0905061D02011908BA012C010100182B4E10F43C4DFD3C4E10F63C4DFD3C003F3C10FD3CFD3C10FD3C31302901112107211121036DFD2602DA96FE5201AE061096FB1C000000000100BCFE8C0430066D00110040402A060A060B060F0610150A1510450B450F590259060A0011130925081011250012087A0D53041912387C182B4E10F44DEDED003FED3FED011239393130015D0124000235341200251506040215141204170430FEEBFE84E3E3017C0115D1FED3ACAC012DD1FE8C11011701DAEEEE01DA0117129C13F3FE88D7D7FE88F2140000000001009DFE8C0411066D00110044402E090A090B090F09101A0A1A104A0B4A0F56025606580B580F0C08090D11250010092508120D53047A0019126C61182B4E10F44DFDED003FED3FED011239393130015D1304001215140200053536241235340224279D0115017CE3E3FE84FEEBD1012DADADFED3D1066D12FEE9FE26EEEEFE26FEE9119B14F20178D7D70178F3130001009DFFD1044F0610001A008A4034390B3B15700270038A07051A1825152C18461056106B0F7A0F7A188A0F9B0FA608AB0FA616B607C615FA0F100B0F08190210131AB801BDB405050D0304B801BBB302010413B801BC40170D0D020303471752091A1C0405620100810F191B5994182B4E10F44DF43CFD3C4E10F64DED76392F183C003FED3F3CFD3C12392FED1139313000715D015D13112115211133200015140604232227351E0133323E0135342421BC0365FD5520014F016A92FEF69696EA55
D25959AA5EFEFFFEB8032702E9B3FE84FEE8ED96EE8749CB2E3B56A55691C90000020047011F0485031700030007002AB9000301BFB2026F07B801BF400C0605001A0907021908202C182B4E10F43C10F63C002F4DFDF6ED313001152135011521350485FBC2043EFBC203179B9BFEA39B9B000000020066FFE1045E046D0014002000E3405CC615E507F40703008904A91ABE09DA1F040D09011F401E0325081516181E0B161B0000011012121F121313000010181E0F4518230B0A0713120A1E3A030B0013161222121369161F100F75701201121A221B2D7006010619214E7E182B4E10F45D4DED4E10F65D4DF43CFDE4111239111239003FED3F3C3F3CEDE41112393987052E2B87087DC40111123900111239393130184379401A191D040908261D041B310019091B2A001C051E31001A07182A012B2B012B2B2B81810049547940121F20010220011E4A041F02154A012015010001103C103C2B002B818101715D00715D250E01232226353412363332171617331114172326031126232202151416333236037955EF648CDF94F8B7356B1020BB2AC2160D6355ACE57D5057D2FB8C8EF2F6C20131B10B0203FCEBCA7E5C017C01DF1AFEF6E5A6A9B0000001009B0000043E064E001700944030C407011F4006131F080316170100133A0607170E0A0F0E1F0C0D0D700B900B020B1A1902171F012F00010019182E50182B4E10F45D3C4DFD3C4E10F65D3C103C4DFD3C003F3C3FED3F11393931304379401607120A0B090B080B0306112612070F3101100B1331012B012B2B2A81004954794012141504051504134A051405164A001516040301103C103C2B002B8181015D331133113E01333216171E0115112311342E0123220607119BBA50E2715F9D1F1912BA1F533162E149064EFD1B819261453577BAFD900287A16742BA8CFD750000000002009E000003C5066D00070013003E401311E50B0101022604030606052607000A08E50EB801F1400C06E8051F02E800191465C9182B4E10F44DE4FDE4F4FD003F3CFD3C3F3CFD3C3FED313001211121352111211501343633321615140623222601D4FECA01F00137FDF0562627565627265603C29BFC3E9B05F03F3E3E3F3E3E3E000001009B0000043E047C0015008F4030C407011F4006111908031415113A06070106150C0A0D0C1F0A0B0B7009900902091A1702151F012F00010019162E50182B4E10F45D3C4DFD3C4E10F65D3C103C4DFD3C003F3C3F3FED113939313043794010071008250F2610070D31010E091131012B012B2B2B81004954794012121304051304114A051205144A001314040301103C103C2B002B8181015D00331133153E0133321E0115112311342E0123220607119BBA50E27163A241BA1F533162E149045DF4819269AAF9FD900287A16742BA8CFD75000000
00020057FFE10476047C000B001700A9405796029A049A08960A04C601C602C604C605C907C908C90AC90BC90DC90EC910C911C613C614C616C617ED01ED05E407E40BFC01FC05F307F30B183708122306070C23000B0F2D700901091A19152D7003010319184E67182B4E10F45D4DED4E10F65D4DED003FED3FED31304379402A01170D0B0F2A011701152A0011070F2A011305152A000E0A0C2A0016020C2A001008122A011404122A012B2B2B2B012B2B2B2B81015D005D0522003534003332001514002732363534262322061514160267F0FEE00120F0EF0120FEE0EF95B0B09596B0B01F014FFFFF014EFEB2FFFFFEB19BE8CBCAE8E8CACBE80002008DFE4E045B047C0012001E00C44051B409C009D102D41D048A058118AC18D218EB05EC07E617FB07081F40031C2508141300031C161314190F0E450A1C3A0307110616230A0B100E192D700601061A20120F1F10102F11A0110211191F2E7E182B4E10F45D3C4D10FD3C4E10F65D4DED003F3FED3F3FED10E40111123939001112173931304379401A171B040908261709192A011B041931011807162A001A051C31012B2B012B2B2B81810049547940121D1E01021E011C4A051D02134A001E13010001103C103C2B002B8181005D015D013E0133321615140206232227262711231133190116333212353426232206014756EE648CE095F8B7346C1020BABA6555A9E77E5057D103628C8EF2F6C2FECFB10B0203FE4E060FFE28FE211A0109E6A7A8B000000100FA00000440047C00110073402B1F40060D1000030B0D0A0806020A0A00020D3A06070206000A0B0A1F0909081A1302111F01001912BF50182B4E10F43C4DFD3C4E10F63C4D10FD3C003F3F3FED1112392F11123911123939123931300049547940120E0F04050F040D4A050E05104A000F10040301103C103C2B002B8181331133153E01333217112335262322060711FABA57E18A6565B32F1B68C85F045DF48A891FFE6DFF08A4A4FD77000000010060FFE1044105C20018007C40138A0087059A009505AA0005190800031809160DB80139B50A1009260F0AB80197400A1623030B006920100110B80186400F0D121F0C07E81F09010919194E50182B4E10F45D4DF43CFD3CF45DE4003FEDFD3CFD3C10E41112391239313043794010041514260525150412310013061631002B012B2B2B8101005D250E0123222E01351121352111331121152111141E01333237044183763775C263FEE90117BA01F1FE0F406B4987952D37155AB0B801C29B01C2FE3E9BFE41876F345500000000010020FE2E04AD045D001200D5409089009900AA00D70304004900590089008A038C04890589129800980397069707AA03AC04AA05B803B904B905C904C905DB04DB05150903010303020404000000010303021212040C120E0201
00001F120300100302061204041F12050506060300031205040402020106120A0E23090F12060403020006013F054F055F056F058F0505051A140C0001010119134D97182B194E10E45D3910E65D11173900183F4DED3F3F3C103C103C12173987052E2B870E7DC487082E182B87057DC400111239871008C4083C871008C4313001715D00715D250133090133010206232227351633323E01370236FDFCCD019B0158BBFE4F89F7C455434D465A8C74182D0430FCBA0346FBF2FEB7D80FA41846B241000001000000020000C0120BB25F0F3CF501110800000000005EE2C58000000000D56A2DA1FB1FFCA2066F09C8000000090001000000000000000100000800FE0000AB04DAFB1FFD74066F00010000000000000000000000000000000E04CD009304CD00BC04CD009D04CD009D04CD004704CD006604CD009B04CD009E04CD009B04CD005704CD008D04CD00FA04CD006004CD002000000038008000C8013A0164020A027C02BE032A03A8043C049404FC058C000000010000000E0070000C004E0005000200100010003C000007E8053E00030001B800322B40212F4E7F4EAF2EAF67042F6B2F95306BCF6BCF95F06B062F3D303DCF3DD03DF03D05B8016AB22D361FBD01F501F60021001F01F401E4B2221F50411B0173000100F00173000100600174007001740080017400E001740004002001740090017400F0017400030050017400B00174000201F1401708321F5108151F0D0B331F0706331F0908311F0302311FB801C3B624191FC024191FB8012FB224191FB801C2B224191F410D01BF01BB0081001F01BD01BB0801001F01BC01BB0081001F01BBB23A811FBC01BA01B90052001F01B9B21F351FB801B8B226811FB801B7B23A381FBC01B6001F0101001F01B5B21F431FBC01B301B40052001F01B4B2242E1FB801B1B224351FB801B0B427811F0840BB01A600000009016AB22D361FB8012AB22D2D1F410B012200620125001F012100620125001F011E00230401B61FE51F231FE33AB80401401B1FE0234A1FBE2D2D1FB9233F1FB823361FA52D2D1FA42DAB1FA352B80401B21FA262B80401B21FA162B80401B21F9F23B80101B21F9E23B80401B61F9B23451F8723B80401B61F85233B1F6E62B80401B21F6362B80401B21F5352B80401B21F4823B80401B61F4723471F4323B80801B21F4223B80401B21F2962B80125B21F2862B80401B21F2623B80401B21F2523B80401400B1F2223431F2123431F1D23B80401403B1F5518091809907707906007904F07904007903E07903107903007902B07902A07901E071408120810080E080C080A080808060804080208000814B8FFE0402B00000100140610000001000604000001000410000001001002000001000200000001000002010802004A00B214201445604418B90001
01FF858D16763F183F123E113946443E113946443E113946443E113946443E11394660443E11394660442B2B2B2B2B2B2B2B2B2B2B182B2B2B2B2B2B2B2B2B2B014B5079BC001F016C0007001F010DB6071FE9071F4A072B2B2B2B4B5379BC0090016C00070090010DB60790E907904A072B2B2B2B181DB0964B5358B0AA1D59B0324B5358B0FF1D594BB09E53205C58B901A801A64544B901A701A645445958B903A401A8455258B901A803A44459594BB09E53205C58B9001F01A84544B9002D01A845445958B9039F001F455258B9001F039F4459594BB8040153205C58B9002401A74544B9003301A745445958B919400024455258B9002419404459594BB8040153205C58B1621F4544B11F1F45445958B917400062455258B9006217404459594BB8080153205C58B1522D4544B12D2D45445958B932800052455258B9005232804459594BB06153205C58B123234544B13A2345445958B901D10023455258B9002301D14459594BB8030153205C58B123234544B1272345445958B90E880023455258B900230E884459594BB8030153205C58B123234544B1392345445958B90E880023455258B900230E884459592B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B6542B33D7D6B95456523456023456560234560B08B766818B080622020B16B7D4565234520B003266062636820B003266165B07D236544B06B234420B13D954565234520B003266062636820B003266165B095236544B03D2344B10095455458B195406544B23D403D4523614459B32E504E67456523456023456560234560B089766818B080622020B14E504565234520B003266062636820B003266165B050236544B04E234420B12E674565234520B003266062636820B003266165B067236544B02E2344B10067455458B167406544B22E402E4523614459456953422B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B2B73747573742B2B2B7373730000
00>] def
/CharStrings 14 dict dup begin
/.notdef 0 def
/parenleft 1 def
/parenright 2 def
/five 3 def
/equal 4 def
/a 5 def
/h 6 def
/i 7 def
/n 8 def
/o 9 def
/p 10 def
/r 11 def
/t 12 def
/y 13 def
 end readonly def
currentdict dup/FontName get exch definefont pop end
%APLsfntEnd
42/FontType resourcestatus{pop pop true}{false}ifelse
{currentfile 0(%APLT1End\n)/SubFileDecode filter flushfile}if
/FontType 1 def
/FontMatrix [ 0.00048828125 0 0 0.00048828125 0 0 ] def
/FontBBox{-1249 -862 1647 2504}def
/UniqueID 4134066 def
currentdict currentfile eexec
54544758EC884CF30C3CD503CEDBFF3839C47C3C3333173232E3FDBFF439491DB843E1924E63AA7726BBB0485AB56D93D8C0906F647A47162891E73FFC2A9873C4B1EAC5EEBDFFC4D06084FBD84139DF4583C6E259D10699944D1068C9C45667DCCCFB9B7EA01B606435EDCBD273ABAC093D14085CCBAC149BD7382E842CFE0D7FE4FD2EF589A2471F6074A80A8B675C2F7A50D63AC1EF90D787BADD11633CB01CF6EE3B37AAF9078A69AC4740E9B6525D78BBD839551A1CB80DB8682FA5E87591BBD6EE8B946063A2A58D9CA3685AB305495DC5FB5747EB8A9A059C4976C0FE4EEAB1D56FF47F1E9664ED9F4A7DAB763AF92B2F6CF2FA7DEC24710E0B9096E30F772BA7FEA9BDBE496C42ED2CEB58F54E80BDF57CE7B4DB6CCFE7182F43BF93CCA0767AF95D62C5D2C3DC6AE1E6D139F51A2C63432117F1714C5566572EE9967A715420ABDCD1D7BD74F8450B89965FCC81C6ACA565C5F3CCF91D430D1F953E4F1A645300A98DD8C47CD64555F08F422340A85404EAE0D3229C4F9336B9470CACBD6BBF3395104750A915CC6EAAC197668267B8C62D2764C8CD69FD937CA3C924D997A0EDE7964BEB9EA2F92EF70C5E5DA0AA5567765E71F2B911B3C5586B741EEB93F3C73016EC16BFF283758900903D203992EFC8BAFAF13579C602F38C91B0B7175CE49F0688B3F79EA3DBC898217EC91EE332F98D08B0D78E002610AC5858EAF625BF678A22AAE4BFA4574E51E71454AD411BD8AFC0E9E9D7E2FA7FF18EE8183E6C5DDE5E76F36D30D564062DA1A6BC31CA0645F3B8B8A044A105730F2EC2C35B0A5FF3122FC9CCAF37CC9E54899A044CC5AC8C275F1F5A4FD3EF584504DF4261508668129A55217F4333DE920CA0CAC167813D9525E5BE15EB6B390AA8D50523E29A8759DE1EC684DE8837A781657B4C124FB5A25CE8A9DFC2A715C75339825BA8518202AFFA3A1F2E18A13F34DDAF9CEAC926FBAC002E2E7AA67855B4E09846AF76A0D4497232F348899830418CDC677820AC38829627E8784DFD7B5ACC687F028274C8E41977C2F8838CED9C25B4E7FF7C45D3C5E4BB5A4750BB4B681D2574F5D13C3A415425109A6E435ACE39DDC9ADF2C62FBF49E64F7BC4AEAE7848FDE1D863E4019869C7802D19BD1C617AC0827DD92AA789237A465E6747B5E2910B800202036AEC298F6877EA055BA8F6296C260432481570511917E38722FE8CEF6CDA6D0AC7B52E022B244E65AB14C49AC9E072647146B0E3DC4AE25522BCEAC4A06B29B7FA78BFAA1E3AE2AE32DC879C01741DAC96193FF14D92A252B9854649009F0707B53A8071E558DBB15C4603EEC49949912F58F87C5A10809263E14213ABF1E3D11BF52AE6753B40461A0D200DEE86F0472C26E7035DDBD6223926D3626F0A1DC15B1300DF3E146DBFC40211D9295A0E3628AABF2D3B5711D7F7E1
A675B2521C3ED023AC8714EDBDE2B5C12F04850F7207573986AE95BF680DDFD33B976FBE5B48199FA7C0A8627135867275C81AE4C57A537592473F45A94C31D83061B6E342101CE7BAA85B53162F35A7325630BF7058D0ECAAB8449E95501BA94AE1C1600DE60425A1BFB8FC5249BF6AFAE502CD36BF678BF474AD4AE2FF0DA5FD88F1A0CAAC68DA51DC1CBD11210767D35EFACE374E08789B68A9823A78CCAF4AC92DC08860CECB450B2B50DA9704F1778D0367342CFB6FEA044575CA7A988C768AB13F5338622B64956AC3C942D6257DAA3238A9B22BCCE0878D8CD5560C91CA50FD8493392FD3B783FF910C979419F584E3D1EC0031CC7D991C46833060EF29C5141DE2D1F5C7D6185E6C2963DA95918B82D8D35025802CFD16E3D9551F523D963D9AAAF4FD80F52B12EDBECAF0B0824033EC4B562C43610F383AB308FC2D788FF7478703DA6534DE4E104AED072EE9172CB6967DAFB88F30F11CBAD502F077AFB597CD016DBC694E5C0BFF5FF0C666AC85A2CFE6019BA2E4D3C0AF82C46C398013CE33A72EACB977414D6CC698A80B985D366E60896E706DF5FDDD97D9470CBAAE0369BEDC2512478014373AF5BEB53B648DD4C23DF70889A90790ACDB99D7469E39B07D524C460ADBC0173126437836C0CB4059C0F0298F1B2E8D419F728F0A22C4B0BCFE0ED403C3C1279C7B60874E98820C3FE3312714A92B28410DF3301760A85CED392AFFD7C704581BBB32F1666649AB7442AB6BEBBFA22829CA4D07B6AF872979842DA7F346FC9A04336FF27EE69A0AD29A174265060231C5CA4D6FEA9E803ECAC97E71088B5729895FB3014A4F9A2DE67959F7CA882A136D96A533EF3A5789ACDA50A67F22A0D648BB6F2198E43CD1C8D8F2B5CF52376F20C94432CE3BFF76DB3AB38CE861FE1DEDC808A25F848538D570262275BBB2E4DF68E99C3535542D07616910847782AC24B88694438CC1278669182127327BFE74AEE775368EA53A1DDF68A427315A219CF50A4E75FC071D6368AD3749571036F7856D1BDE6D15FE067559D1B2078C170556EE2090DEE8FB9D0A1EC0109BA24FFEA7A7E92A3461858E1BB6DB60E74B3689C8E310F48AF03B7D531A9619C6C61DD69A50D78835BCC8DA001EA1FF98BA0A902A569EC378E3589B3870404C140C390EA1F15E61BA11B8D5A0814E978841D5B57A11A7046D6917551D58AEF325D9F65696FDAA6533A018C300B994DA7C38835CCC4079A37AF9B82BABDEFA7F0002D582234D5A1E1D573B7B9C49CDED047089355DF6EFD21F934073B4A276176992A0338A4571644437357C34133C80C4A36EABA3ABDB490969BE225533B8D0DB86E4AE1E8FE9CFA01BBD97926C1166D6CA2C8246F94B117B68A66AE35EA4787A75809CC0D9324CFD3C4BC811145E1573C4072FF723833663C1273D3EA85D773F0FA0E6DC75
A3DE42EEF0D9771883228F690F9CE7E7AB400929F13D47746A260ADA7063C1AC94D06FC121BEEA0DDD2F49421E745814D808FCFD59C540B7C7B82C8AFD99A68C861706CA68FA565979A50BF14D922DD6D7910E65779AF30FA278C8003D42434A53BFEB3F0C15AD5DC3432D23C31DD6EB10F5FFF7589139C62F5D0926D7E130EED057426D1A8198FEBB8877EA1D5198953F1D986F61C1254354FDA7CA62373773B3DE11958EF83BDBE9350960FC811BDDC4A8FC64AADBA393F1C68519F5DA28B0F612C231FB474014DC95C50881EC3F42FF6B5B8B9B5721125FA68EC465273BFD13A519B7884B50B900718F0D609FFDBD7D1364C452AE4605AF6A54433E0A48760E0DC3355E620EDB4AC47730960B0CB9543FBADB2FB4BB1E86C86A310EB60B5CA260EFB207B8B08EDA734076778C19976A67CB09E7442B64C69F9407D7864BA784EA087278E63221974DED53389B69CA8AA5C5AF343EB64B8EAAFCC66651AD9BC81C6CF14B77DF92A34CF3AEB1E38E53392F70ACC381EACD56F8186EAF1F7F42D860F4B59EFA937A88D3BF99782B3DE4B118BA6E76
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000000000000000000000000000000
cleartomark end
%APLT1End
%RBIEndFontSubset
/PQWPDK+Monaco cguidfix
/F1.1/PQWPDK+Monaco renmfont
[ /CIEBasedABC 4 dict dup begin 
/WhitePoint [ 0.9505 1.0000 1.0891 ] def 
/DecodeABC [ 
{ 1.0 0.0 3 -1 roll 1 index 1 index le { exch pop} { pop } ifelse 
 1 index 1 index ge { exch pop } { pop } ifelse < 
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000001010101010101010101010101
0101010101010101010101010101010101010101010101020202020202020202
0202020202020202020202020202020202030303030303030303030303030303
0303030303030304040404040404040404040404040404040404050505050505
0505050505050505050506060606060606060606060606060607070707070707
0707070707070708080808080808080808080808090909090909090909090909
0a0a0a0a0a0a0a0a0a0a0a0b0b0b0b0b0b0b0b0b0b0b0c0c0c0c0c0c0c0c0c0c
0d0d0d0d0d0d0d0d0d0d0e0e0e0e0e0e0e0e0e0f0f0f0f0f0f0f0f0f10101010
1010101010111111111111111112121212121212121313131313131313141414
1414141414151515151515151616161616161616171717171717171818181818
18181919191919191a1a1a1a1a1a1a1b1b1b1b1b1b1c1c1c1c1c1c1c1d1d1d1d
1d1d1e1e1e1e1e1e1f1f1f1f1f1f202020202020212121212121222222222223
2323232323242424242425252525252526262626262727272727282828282829
292929292a2a2a2a2a2b2b2b2b2b2c2c2c2c2c2d2d2d2d2d2e2e2e2e2e2f2f2f
2f2f303030303131313131323232323333333333343434343535353535363636
36373737373838383839393939393a3a3a3a3b3b3b3b3c3c3c3c3d3d3d3d3e3e
3e3e3f3f3f3f4040404041414141424242424343434444444445454545464646
4647474748484848494949494a4a4a4b4b4b4b4c4c4c4d4d4d4d4e4e4e4f4f4f
4f50505051515151525252535353535454545555555656565657575758585859
59595a5a5a5a5b5b5b5c5c5c5d5d5d5e5e5e5f5f5f6060606061616162626263
63636464646565656666666767676868686969696a6a6a6b6b6b6c6c6d6d6d6e
6e6e6f6f6f707070717171727273737374747475757576767677777878787979
797a7a7b7b7b7c7c7c7d7d7e7e7e7f7f7f808081818182828283838484848585
86868687878888888989898a8a8b8b8b8c8c8d8d8d8e8e8f8f90909091919292
9293939494949595969697979798989999999a9a9b9b9c9c9c9d9d9e9e9f9f9f
a0a0a1a1a2a2a3a3a3a4a4a5a5a6a6a6a7a7a8a8a9a9aaaaabababacacadadae
aeafafb0b0b0b1b1b2b2b3b3b4b4b5b5b6b6b6b7b7b8b8b9b9bababbbbbcbcbd
bdbebebebfbfc0c0c1c1c2c2c3c3c4c4c5c5c6c6c7c7c8c8c9c9cacacbcbcccc
cdcdcececfcfd0d0d1d1d2d2d3d3d4d4d5d5d6d6d7d7d8d8d9d9dadadbdcdcdd
dddededfdfe0e0e1e1e2e2e3e3e4e4e5e6e6e7e7e8e8e9e9eaeaebebecededee
eeefeff0f0f1f1f2f3f3f4f4f5f5f6f6f7f8f8f9f9fafafbfcfcfdfdfefeffff
>  dup length 1 sub 3 -1 roll mul dup dup floor cvi exch ceiling 
 cvi 3 index exch get 4 -1 roll 3 -1 roll get
 dup 3 1 roll sub 3 -1 roll dup floor cvi sub mul add 255 div } bind 

{ 1.0 0.0 3 -1 roll 1 index 1 index le { exch pop} { pop } ifelse 
 1 index 1 index ge { exch pop } { pop } ifelse < 
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000001010101010101010101010101
0101010101010101010101010101010101010101010101020202020202020202
0202020202020202020202020202020202030303030303030303030303030303
0303030303030304040404040404040404040404040404040404050505050505
0505050505050505050506060606060606060606060606060607070707070707
0707070707070708080808080808080808080808090909090909090909090909
0a0a0a0a0a0a0a0a0a0a0a0b0b0b0b0b0b0b0b0b0b0b0c0c0c0c0c0c0c0c0c0c
0d0d0d0d0d0d0d0d0d0d0e0e0e0e0e0e0e0e0e0f0f0f0f0f0f0f0f0f10101010
1010101010111111111111111112121212121212121313131313131313141414
1414141414151515151515151616161616161616171717171717171818181818
18181919191919191a1a1a1a1a1a1a1b1b1b1b1b1b1c1c1c1c1c1c1c1d1d1d1d
1d1d1e1e1e1e1e1e1f1f1f1f1f1f202020202020212121212121222222222223
2323232323242424242425252525252526262626262727272727282828282829
292929292a2a2a2a2a2b2b2b2b2b2c2c2c2c2c2d2d2d2d2d2e2e2e2e2e2f2f2f
2f2f303030303131313131323232323333333333343434343535353535363636
36373737373838383839393939393a3a3a3a3b3b3b3b3c3c3c3c3d3d3d3d3e3e
3e3e3f3f3f3f4040404041414141424242424343434444444445454545464646
4647474748484848494949494a4a4a4b4b4b4b4c4c4c4d4d4d4d4e4e4e4f4f4f
4f50505051515151525252535353535454545555555656565657575758585859
59595a5a5a5a5b5b5b5c5c5c5d5d5d5e5e5e5f5f5f6060606061616162626263
63636464646565656666666767676868686969696a6a6a6b6b6b6c6c6d6d6d6e
6e6e6f6f6f707070717171727273737374747475757576767677777878787979
797a7a7b7b7b7c7c7c7d7d7e7e7e7f7f7f808081818182828283838484848585
86868687878888888989898a8a8b8b8b8c8c8d8d8d8e8e8f8f90909091919292
9293939494949595969697979798989999999a9a9b9b9c9c9c9d9d9e9e9f9f9f
a0a0a1a1a2a2a3a3a3a4a4a5a5a6a6a6a7a7a8a8a9a9aaaaabababacacadadae
aeafafb0b0b0b1b1b2b2b3b3b4b4b5b5b6b6b6b7b7b8b8b9b9bababbbbbcbcbd
bdbebebebfbfc0c0c1c1c2c2c3c3c4c4c5c5c6c6c7c7c8c8c9c9cacacbcbcccc
cdcdcececfcfd0d0d1d1d2d2d3d3d4d4d5d5d6d6d7d7d8d8d9d9dadadbdcdcdd
dddededfdfe0e0e1e1e2e2e3e3e4e4e5e6e6e7e7e8e8e9e9eaeaebebecededee
eeefeff0f0f1f1f2f3f3f4f4f5f5f6f6f7f8f8f9f9fafafbfcfcfdfdfefeffff
>  dup length 1 sub 3 -1 roll mul dup dup floor cvi exch ceiling 
 cvi 3 index exch get 4 -1 roll 3 -1 roll get
 dup 3 1 roll sub 3 -1 roll dup floor cvi sub mul add 255 div } bind 

{ 1.0 0.0 3 -1 roll 1 index 1 index le { exch pop} { pop } ifelse 
 1 index 1 index ge { exch pop } { pop } ifelse < 
0000000000000000000000000000000000000000000000000000000000000000
0000000000000000000000000000000000000001010101010101010101010101
0101010101010101010101010101010101010101010101020202020202020202
0202020202020202020202020202020202030303030303030303030303030303
0303030303030304040404040404040404040404040404040404050505050505
0505050505050505050506060606060606060606060606060607070707070707
0707070707070708080808080808080808080808090909090909090909090909
0a0a0a0a0a0a0a0a0a0a0a0b0b0b0b0b0b0b0b0b0b0b0c0c0c0c0c0c0c0c0c0c
0d0d0d0d0d0d0d0d0d0d0e0e0e0e0e0e0e0e0e0f0f0f0f0f0f0f0f0f10101010
1010101010111111111111111112121212121212121313131313131313141414
1414141414151515151515151616161616161616171717171717171818181818
18181919191919191a1a1a1a1a1a1a1b1b1b1b1b1b1c1c1c1c1c1c1c1d1d1d1d
1d1d1e1e1e1e1e1e1f1f1f1f1f1f202020202020212121212121222222222223
2323232323242424242425252525252526262626262727272727282828282829
292929292a2a2a2a2a2b2b2b2b2b2c2c2c2c2c2d2d2d2d2d2e2e2e2e2e2f2f2f
2f2f303030303131313131323232323333333333343434343535353535363636
36373737373838383839393939393a3a3a3a3b3b3b3b3c3c3c3c3d3d3d3d3e3e
3e3e3f3f3f3f4040404041414141424242424343434444444445454545464646
4647474748484848494949494a4a4a4b4b4b4b4c4c4c4d4d4d4d4e4e4e4f4f4f
4f50505051515151525252535353535454545555555656565657575758585859
59595a5a5a5a5b5b5b5c5c5c5d5d5d5e5e5e5f5f5f6060606061616162626263
63636464646565656666666767676868686969696a6a6a6b6b6b6c6c6d6d6d6e
6e6e6f6f6f707070717171727273737374747475757576767677777878787979
797a7a7b7b7b7c7c7c7d7d7e7e7e7f7f7f808081818182828283838484848585
86868687878888888989898a8a8b8b8b8c8c8d8d8d8e8e8f8f90909091919292
9293939494949595969697979798989999999a9a9b9b9c9c9c9d9d9e9e9f9f9f
a0a0a1a1a2a2a3a3a3a4a4a5a5a6a6a6a7a7a8a8a9a9aaaaabababacacadadae
aeafafb0b0b0b1b1b2b2b3b3b4b4b5b5b6b6b6b7b7b8b8b9b9bababbbbbcbcbd
bdbebebebfbfc0c0c1c1c2c2c3c3c4c4c5c5c6c6c7c7c8c8c9c9cacacbcbcccc
cdcdcececfcfd0d0d1d1d2d2d3d3d4d4d5d5d6d6d7d7d8d8d9d9dadadbdcdcdd
dddededfdfe0e0e1e1e2e2e3e3e4e4e5e6e6e7e7e8e8e9e9eaeaebebecededee
eeefeff0f0f1f1f2f3f3f4f4f5f5f6f6f7f8f8f9f9fafafbfcfcfdfdfefeffff
>  dup length 1 sub 3 -1 roll mul dup dup floor cvi exch ceiling 
 cvi 3 index exch get 4 -1 roll 3 -1 roll get
 dup 3 1 roll sub 3 -1 roll dup floor cvi sub mul add 255 div } bind 
] def 
/MatrixABC [ 0.4124 0.2126 0.0193 0.3576 0.7151 0.1192 0.1805 0.0722 0.9508 ] def 
/RangeLMN [ 0.0 0.9505 0.0 1.0000 0.0 1.0891 ] def 
end ] /Cs1 exch/ColorSpace dr pop
%%EndPageSetup
/Cs1 SC
1 1 1 sc
q
71.999992 676.69983 451 75.300179 rc
71.999992 752 m
523 752 l
523 676.69983 l
71.999992 676.69983 l
h
f
0 0 0 sc
0.80106568 0 0 -0.80106568 71.999992 752 cm
/F1.1[ 11 0 0 -11 0 0]sf
8 19 m
(!"#)[ 6.601100 6.601100 0.000000 ] xS
8 34 m
($%&'\(\)!*)[ 6.601100 6.601100 6.601100 6.601100 6.601100 6.601100 6.601100 0.000000 ] xS
8 49 m
($+\(,-')[ 6.601100 6.601100 6.601100 6.601100 6.601100 0.000000 ] xS
8 64 m
(!"#)[ 6.601100 6.601100 0.000000 ] xS
8 79 m
($%&'\(\)!*)[ 6.601100 6.601100 6.601100 6.601100 6.601100 6.601100 6.601100 0.000000 ] xS
ep
end
%%Trailer
%%Pages: 1
%%BoundingBox: 0 0 595 842
%%EOF
