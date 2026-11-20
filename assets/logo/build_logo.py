import random, traceback
from gi.repository import Gimp, Gegl, Gio
LOG=lambda *a: open("./out.txt","a").write(" ".join(map(str,a))+"\n")
random.seed(7)
GOLD="#d4a017"; GOLD_HI="#ffd95a"; GOLD_LO="#a8780a"
try:
    W,H=2000,1000
    img=Gimp.Image.new(W,H,Gimp.ImageBaseType.RGB)
    def C(c): return Gegl.Color.new(c)
    def newlayer(name,pos=0):
        l=Gimp.Layer.new(img,name,W,H,Gimp.ImageType.RGBA_IMAGE,100,Gimp.LayerMode.NORMAL)
        img.insert_layer(l,None,pos); l.fill(Gimp.FillType.TRANSPARENT); return l
    def fill(l,c):
        Gimp.context_set_foreground(C(c)); l.edit_fill(Gimp.FillType.FOREGROUND)
    def text(s,font,size,color,x,y):
        t=Gimp.TextLayer.new(img,s,Gimp.Font.get_by_name(font),size,Gimp.Unit.pixel())
        img.insert_layer(t,None,0); t.set_color(C(color)); t.set_offsets(x,y); return t
    def poly(l,pts,c,op=Gimp.ChannelOps.REPLACE):
        img.select_polygon(op,pts); fill(l,c); Gimp.Selection.none(img)
    def ell(l,x,y,w,h,c):
        img.select_ellipse(Gimp.ChannelOps.REPLACE,x,y,w,h); fill(l,c); Gimp.Selection.none(img)

    # --- background: near-black with faded repeating wordmark pattern
    bg=newlayer("Background"); bg.fill(Gimp.FillType.TRANSPARENT); fill_all=True
    img.select_rectangle(Gimp.ChannelOps.REPLACE,0,0,W,H); fill(bg,"#0d0d0f"); Gimp.Selection.none(img)
    pats=[]
    LOG("start")
    for row in range(-3,14):
        for col in range(0,1):
            s="  ".join(["BEAST-MODELL"]*6)
            t=text(s,"Rubik Wet Paint Regular",78,"#1d1d22",
                   -400+(row%2)*-260, row*92)
            t.transform_rotate(-0.12,True,0,0)
            pats.append(t)
    pl=pats[0]
    for t in pats[1:]:
        pl=img.merge_down(t,Gimp.MergeType.CLIP_TO_IMAGE) if False else pl
    # merge pattern layers into one
    for t in reversed(pats[:-1]):
        pass
    grp=None
    # simple approach: merge each down repeatedly from top
    while True:
        top=img.get_layers()[0]
        if top.get_name()=="Background": break
        nxt=img.get_layers()[1]
        if nxt.get_name()=="Background":
            top.set_name("Pattern"); break
        img.merge_down(top,Gimp.MergeType.CLIP_TO_IMAGE)
    pattern=img.get_layers()[0]; pattern.resize_to_image_size(); LOG("pattern done")

    # --- art layers
    grid=newlayer("Grid",0)
    scratch=newlayer("Claw marks",0)
    # main wordmark
    S=300
    beast=text("BEAST","Rubik Wet Paint Regular",S,"#0a0a0a",0,0)
    bx=(W-beast.get_width())//2-40; beast.set_offsets(bx,150)
    m=text("M","Rubik Wet Paint Regular",S,"#0a0a0a",0,0)
    o=text("O","Rubik Wet Paint Regular",S,"#0a0a0a",0,0)
    de=text("DE","Rubik Wet Paint Regular",S,"#0a0a0a",0,0)
    ll=text("L","Rubik Wet Paint Regular",S,GOLD,0,0)
    ll2=text("L","Rubik Wet Paint Regular",S,GOLD,0,0)
    gap=-18
    total=m.get_width()+o.get_width()+de.get_width()+ll.get_width()+ll2.get_width()+4*gap
    x=(W-total)//2+40; y=150+int(S*0.92)
    for t in (m,o,de,ll,ll2):
        t.set_offsets(x,y); x+=t.get_width()+gap
    for t in (ll,ll2):
        gl=newlayer("Gold "+t.get_name(),0)
        img.select_item(Gimp.ChannelOps.REPLACE,t)
        try:
            Gimp.context_set_foreground(C(GOLD_HI)); Gimp.context_set_background(C(GOLD_LO))
            Gimp.context_set_gradient_fg_bg_rgb()
            ty=t.get_offsets()[2]
            gl.edit_gradient_fill(Gimp.GradientType.LINEAR,0,False,1,0.0,True,0,ty+40,0,ty+t.get_height()-20)
        except Exception as e:
            LOG("gradient fail",e); fill(gl,GOLD)
        Gimp.Selection.none(img)
    LOG("sizes",beast.get_width(),beast.get_height(),m.get_width(),o.get_width(),de.get_width(),ll.get_width(),"y2",y)
    # Wolverine-style claw print over the O: three parallel tapered gold slashes
    ox,oy=o.get_offsets()[1:]; ow,oh=o.get_width(),o.get_height()
    paw=newlayer("Claw print",0)
    cx,cy=ox+ow/2, oy+oh*0.55; r=min(ow,oh)*0.36
    ell(paw,cx-r,cy-r,2*r,2*r,"#0a0a0a")
    import math
    ang=math.radians(-62)              # slash direction (lower-left to upper-right)
    ux,uy=math.cos(ang),math.sin(ang); nx,ny=-uy,ux
    L=r*1.9; sp=r*0.5; wmax=r*0.21
    for k in (-1,0,1):
        mx,my=cx+nx*sp*k, cy+ny*sp*k
        half=L*(0.5 if k==0 else 0.44)
        pts=[]
        steps=12
        for i in range(steps+1):
            t=-1+2*i/steps; w=wmax*(1-t*t)**0.8*(1.0 if k==0 else 0.9)
            pts+= [mx+ux*half*t+nx*w, my+uy*half*t+ny*w]
        for i in range(steps,-1,-1):
            t=-1+2*i/steps; w=wmax*(1-t*t)**0.8*(1.0 if k==0 else 0.9)*0.35
            pts+= [mx+ux*half*t-nx*w, my+uy*half*t-ny*w]
        poly(paw,pts,GOLD_HI)
        # darker gold shading on the trailing edge
        sh=[]
        for i in range(steps+1):
            t=-1+2*i/steps; w=wmax*(1-t*t)**0.8*0.35
            sh+= [mx+ux*half*t+nx*w*0.2, my+uy*half*t+ny*w*0.2]
        for i in range(steps,-1,-1):
            t=-1+2*i/steps; w=wmax*(1-t*t)**0.8*0.35
            sh+= [mx+ux*half*t-nx*w, my+uy*half*t-ny*w]
        poly(paw,sh,GOLD_LO)
    # grid lines behind letters (slanted)
    gx0,gy0,gx1,gy1=bx-20,170,bx+beast.get_width()+60,y+m.get_height()-40
    for i in range(0,9):
        xx=gx0+i*(gx1-gx0)/8
        poly(grid,[xx,gy0,xx+3,gy0,xx-60+3,gy1,xx-60,gy1],"#9a9a9a")
    for j in range(0,6):
        yy=gy0+j*(gy1-gy0)/5
        poly(grid,[gx0,yy+20,gx1,yy-20,gx1,yy-17,gx0,yy+23],"#9a9a9a")
    # claw slashes (red) across top-right and bottom-left
    def claw(x0,y0,dx,dy,n,c):
        for k in range(n):
            ox_=x0+k*34; oy_=y0+k*20
            poly(scratch,[ox_,oy_,ox_+dx,oy_+dy,ox_+dx+8,oy_+dy-14,ox_+14,oy_-4],c)
    claw(gx1-120,200,200,-70,3,GOLD)
    claw(gx0-90,y+m.get_height()-60,200,-60,3,GOLD)
    # splatter dots
    for _ in range(70):
        sx=random.randint(gx0-80,gx1+80); sy=random.randint(120,y+m.get_height())
        rr=random.choice([4,6,8,10,14])
        ell(scratch,sx,sy,rr,rr,"#0a0a0a")
    # tagline
    tag=text("NEVER GUESS.  ALWAYS VERIFY.","Permanent Marker Regular",64,"#0a0a0a",0,0)
    tag.set_offsets((W-tag.get_width())//2, y+m.get_height()-20)

    LOG("art done")
    # --- merge art into one layer, keep copies as editable layers? merge for sticker
    art_layers=[l for l in img.get_layers() if l.get_name() not in ("Background","Pattern","Claw marks")]
    # build sticker silhouette from union of art
    Gimp.Selection.none(img)
    for l in art_layers:
        img.select_item(Gimp.ChannelOps.ADD,l)
    img.select_item(Gimp.ChannelOps.ADD,img.get_layer_by_name("Claw marks"))
    Gimp.Selection.grow(img,46); Gimp.Selection.flood(img)
    sticker=newlayer("Sticker",len(art_layers)+1)
    fill(sticker,"#ffffff")
    Gimp.Selection.grow(img,8)
    outline=newlayer("Sticker outline",len(art_layers)+2)
    fill(outline,GOLD)
    Gimp.Selection.grow(img,4)
    shadow=newlayer("Shadow",len(art_layers)+3)
    fill(shadow,"#000000"); Gimp.Selection.none(img)
    shadow.set_offsets(14,18); shadow.set_opacity(70)
    try:
        f=Gimp.DrawableFilter.new(shadow,"gegl:gaussian-blur","Blur")
        cfg=f.get_config(); cfg.set_property("std-dev-x",14.0); cfg.set_property("std-dev-y",14.0)
        shadow.merge_filter(f)
    except Exception as e: LOG("blur fail",e)

    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE,img,Gio.File.new_for_path("./beast-modell-logo.xcf"),None)
    dup=img.duplicate(); dup.merge_visible_layers(Gimp.MergeType.CLIP_TO_IMAGE)
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE,dup,Gio.File.new_for_path("./beast-modell-banner.png"),None)
    # transparent sticker-only version
    d2=img.duplicate()
    for l in d2.get_layers():
        if l.get_name() in ("Background","Pattern"): l.set_visible(False)
    d2.merge_visible_layers(Gimp.MergeType.CLIP_TO_IMAGE)
    for l in d2.get_layers():
        if not l.get_visible(): d2.remove_layer(l)
    d2.get_layers()[0].resize_to_image_size()
    lay=d2.get_layers()[0]
    d2.select_item(Gimp.ChannelOps.REPLACE,lay)
    ok,empty,x1,y1,x2,y2=Gimp.Selection.bounds(d2)
    Gimp.Selection.none(d2)
    d2.crop(x2-x1+24,y2-y1+24,x1-12,y1-12)
    Gimp.file_save(Gimp.RunMode.NONINTERACTIVE,d2,Gio.File.new_for_path("./beast-modell-sticker.png"),None)
    LOG("OK")
except Exception:
    LOG(traceback.format_exc())
