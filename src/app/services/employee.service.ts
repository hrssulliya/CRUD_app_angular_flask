import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class EmployeeService {

  constructor(private _http: HttpClient) { }
  
  // addEmployee(data:any): Observable<any>{
  //   return this._http.post('http://localhost:3000/employees', data);
  // }

  addEmployee(data:any): Observable<any>{
    return this._http.post('http://127.0.0.1:5555/user', data);
  }



  // updateEmployee(id:number, data:any): Observable<any>{
  //   return this._http.put(`http://localhost:3000/employees/${id}`, data);
  // }

  updateEmployee(id:number, data:any): Observable<any>{
    return this._http.put(`http://127.0.0.1:5555/update_user/${id}`, data);
  }

  // getEmployeeList(): Observable<any>{
  //   return this._http.get('http://localhost:3000/employees' );
  // }

  getEmployeeList(): Observable<any>{
    return this._http.get('http://127.0.0.1:5555/get_user' );
  }

  // deleteEmployee(id:number): Observable<any>{
  //   return this._http.delete(`http://localhost:3000/employees/${id}`);
  // }

  deleteEmployee(id:number): Observable<any>{
    return this._http.delete(`http://127.0.0.1:5555/delete_user/${id}`);
  }
}
