import React from 'react'

function Home() {
  return (
    <div>
    <main className="mt-5">
 <div className="container">
   <section className="text-center">
     <div className="row">
       
         
       <div  className="col-lg-4 col-md-12 mb-4">
         <div className="card">
           <div
             className="bg-image hover-zoom ripple"
             data-mdb-ripple-color="light"
           >
            <Link to=''>
             <img
               src=''
               className="w-100"
               alt='Restaurant image'
             />
             </Link>
             <a href="#!">
               <div className="mask">
                 <div className="d-flex justify-content-start align-items-end h-100">
                   <h5>
                     <span className="badge badge-primary ms-2">New</span>
                   </h5>
                 </div>
               </div>
               <div className="hover-overlay">
                 <div
                   className="mask"
                   style={{ backgroundColor: "rgba(251, 251, 251, 0.15)" }}
                 />
               </div>
             </a>
           </div>
           <div className="card-body">
            <Link to='' className="text-reset">

               <h5 className="card-title mb-3">Lords Hotel</h5>
               </Link>
             <a href="" className="text-reset">
               
             </a>
             
             
           </div>
         </div>
       </div>
       
       

       <div className='row'>
        
          
         <div className="col-lg-2">
           <img src=''   style={{ width: "100px", height: "100px", borderRadius: "50%", objectFit: "cover" }} alt="Category Image" />
           <h6>Desi</h6>
         </div>
        
         
       </div>

     </div>
   </section>
   {/*Section: Wishlist*/}
 </div>
</main>
 </div>
  )
}

export default Home